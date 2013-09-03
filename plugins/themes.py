# -*- coding: utf-8 -*-

# Copyright © 2013 Puneeth Chaganti

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import unicode_literals

import codecs
import os
import datetime
import json

from doit.tools import timeout

from nikola.plugin_categories import Task
from nikola import utils


class Theme(Task):
    """Change theme using random flickr image and base color."""

    name = "theme"
    sources_folder = "less"

    def gen_tasks(self):
        """Tweak theming by generating a LESS definition file."""

        template = self.site.config.get('LESS_THEME_TEMPLATE', '')
        if not template:
            print('No less theme template found... exiting.')
            yield {'basename': self.name, 'actions':[]}
            return
        timeout_time = self.site.config.get('THEME_TIMEOUT',
                                            datetime.timedelta(days=1))

        kw = {
            'cache_folder': self.site.config['CACHE_FOLDER'],
            'themes': self.site.THEMES,
            'template': template,
        }

        # Build targets and write CSS files
        base_path = utils.get_theme_path(self.site.THEMES[0])
        dst_dir = os.path.join(base_path, self.sources_folder)
        target = os.path.join(dst_dir, 'define.less')
        json_target = os.path.join(self.site.config['OUTPUT_FOLDER'], 'assets',
                                   'js', 'background_image_data.json')

        def write_theme_define():
            """ Write the theme file and json data file.
            """
            try:
                image_data = get_random_image()
                bg_url = image_data['url'].strip()
                thumbnail = image_data['thumbnail_url'].strip()
                base_color = color_from_url(thumbnail)
            except Exception as e:
                print 'Failed to change image.'
                print e
                return {'basename': self.name, 'actions':[]}
            with codecs.open(target, "w", "utf-8") as f:
                f.write(template % (base_color, bg_url))
            with codecs.open(json_target, "w", "utf-8") as f:
                json.dump(image_data, f, indent=2)

        yield {
                'basename': self.name,
                'name': target,
                'targets': [target, json_target],
                'actions': [(write_theme_define, [])],
                'uptodate': [timeout(timeout_time),
                             os.path.exists(target),
                             utils.config_changed(kw)],
                'clean': True,
                'verbosity': 2,
            }


def get_random_image(retries=5):
    """ Fetch a random image from flickr.

    XXX: Change the search term to an argument
    """
    import micawber
    import lxml.html
    from random import choice
    #from urllib2 import urlopen
    FLICKR = 'http://www.flickr.com'
    SEARCH = '/search/?q=ultimate frisbee %s&l=cc&ct=0&mt=photos&adv=1&page=%d'
    TERMS = ['throw', 'catch', 'layout', 'bid']

    #def get_random_image():
    term = choice(TERMS)
    page = choice(range(1, 6))
    search = SEARCH % (term, page)
    print 'Searching for images on Flickr...'
    tree = lxml.html.parse('%s%s' % (FLICKR, search))
    photos = [e for e in tree.findall(".//a[@data-track]") if e.attrib['data-track'] == 'photo-click']

    found = False
    count = 0

    print 'Getting thumbnail and url for random image...',
    while not found and count < retries:
        count += 1
        the_photo = choice(photos)
        photo_url = FLICKR + the_photo.attrib['href']

        # FIXME: Catch any possible errors
        providers = micawber.bootstrap_basic()
        data = providers.request(photo_url)

        found = 'thumbnail_url' in data and 'url' in data
    print 'done'
    return data

def get_image_buffer(url):
    from urllib import urlopen
    from StringIO import StringIO
    return StringIO(urlopen(url).read())


def get_image(path_or_buf):
    """ Get an Image.Image instance given path or buffer.
    """
    Image = None
    try:
        import Image
    except ImportError:
        try:
            from PIL import Image
        except ImportError:
            pass
    if Image is None:
        print('Install PIL to use the plugin.')
        return

    return Image.open(path_or_buf)

def get_dominant_color(im):
    """ Returns the dominant color of the given image

    Uses a trivial binning algorithm using some pre-defined colors.
    """

    from random import choice

    def distance(c1, c2):
        sum = 0
        for i, val in enumerate(c1):
            sum += ((val - c2[i]) * (val - c2[i]))
        return sum

    COLORS = [
        # Reds
        (247, 62, 42),
        (220, 53, 34),
        (242, 154, 46),
        (248, 143, 27),

        # Greens
        (94, 166, 4),
        (158, 204, 7),
        (27, 174, 106),
        (22, 140, 140),

        # Blues
        (29, 98, 199),
        (121, 117, 227),
        (1, 72, 190),
        (152, 218, 253),
        ]

    bins = [0] * len(COLORS)

    im_data = im.getdata()
    for i in range(min(1000, len(im_data))):
        pixel = choice(im_data)
        idx, dist = 0, 200000
        for j, color in enumerate(COLORS):
            d = distance(color, pixel)
            if d < dist:
                idx = j
                dist = d
        bins[idx] += 1

    max_color = COLORS[bins.index(max(bins))]

    return 'rgb%s' % (max_color, )

color_from_url = lambda x: get_dominant_color(get_image(get_image_buffer(x)))


if __name__ == "__main__":
    data = get_random_image()
    print data
    thumbnail = data['thumbnail_url']
    print thumbnail
    print color_from_url(thumbnail)

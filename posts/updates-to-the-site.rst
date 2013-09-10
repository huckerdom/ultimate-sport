.. description: A note on some of the updates to the site
.. tags: site, logo, design, updates
.. title: Updates to the site
.. link: 
.. author: punchagan
.. date: 2013/09/13 08:00:00
.. slug: updates-to-the-site

This is not really a post on Ultimate, but just a note on some of the
changes I made to the site.  I've spent quite a bit of time on the new
theme, and I like the way it has turned out.  I know, some of you are
thinking, I could've gone to the field and got in some throws instead!

You can skip the rest of the post, if you are not interested in the
details of how the site is published and the theme.  But, for the
interested, here are the details.

The site is powered by `Nikola <http://getnikola.com>`_, a static site
generator, written in Python.  The posts are written in plain text
using `reStructured text <http://docutils.sourceforge.net/rst.html>`_.
Anybody can contribute to the site, either by forking the repository
on GitHub and sending us a pull request, or just leave a comment on
this post, and we'll get back to you. 

The theme is `here <https://github.com/huckerdom/nyck>`_. It is a mix
of twitter's look and the `Lagom4ni
<https://github.com/punchagan/lagom4ni>`_ theme.  The theme changes
the background image automatically, by `fetching a random image
<https://github.com/huckerdom/ultimate-sport/blob/master/plugins/themes.py#L100>`_
from Flickr.  Also, the image is analyzed to find the dominant color
of the image and style the rest of the looks of the site.  The bottom
of the page, contains a link to the original image on Flickr.  I'm not
responsible for any images that look inappropriate. ;)

Finally, I've also designed a `new logo
<https://github.com/huckerdom/huckimg/blob/master/ultimate-sport-512.png>`_
for the site.  It is a shameless ripoff of the "I <3 NY" theme.  The
skying image is a derivative of `this photograph
<http://www.flickr.com/photos/damclean/260337381/>`_.  Any suggestions
to improve the logo are welcome!

Thanks to `@kkrovvidi <https://twitter.com/kkrovvidi>`_, `@baali_
<https://twitter.com/baali_>`_, `@cloud9trt
<https://twitter.com/cloud9trt>`_, `@riteshsaini
<https://twitter.com/riteshsaini>`_ and everyone else, who helped with
the logo and the theme design.

Also, I wish to update the post regularly.  I've even managed to get a
new `scheduling feature <https://github.com/ralsina/nikola/pull/602>`_
added to Nikola, for this!  I `plan to update
<https://github.com/huckerdom/ultimate-sport/blob/f37ef6fb8e34541c2086b417fc4390b7a4d3cc33/conf.py#L323>`_
the site every Monday, Wednesday and Friday at 8 am.  I wouldn't mind
a poke or two, from the readers, if I go out of schedule!  Thank you!

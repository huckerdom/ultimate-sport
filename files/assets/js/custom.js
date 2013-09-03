// Google's Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-40178496-1', 'ultimatesport.in');
  ga('send', 'pageview');

// Tipuesearch
$(document).ready(function() {
    $('#tipue_search_input').tipuesearch({
        'mode': 'json',
        'contentLocation': '/assets/js/tipuesearch_content.json',
        'showUrl': false
    });
});

// Add background image data to footer
$(document).ready(function() {
    jQuery.getJSON('/assets/js/background_image_data.json', function(data) {
        console.log(data);
        var footer = $('.footer');
        var img_link = $('<a>').attr('href', data.web_page).attr('target', '_blank');
        img_link.text(data.author_name)
        $('<small>').appendTo(footer).append($('<p>').text('Random background image by ').append(img_link));
    });
});

// Tag cloud
$(document).ready(function() {
    jQuery.getJSON('/assets/js/tag_cloud_data.json', function(data) {
        var items = [];
        var weights = [];

        $.each(data, function(key, val) {
            weights.push(val[0]);
        });

        var min = Math.min.apply(null, weights);
        var max = Math.max.apply(null, weights);
        var bins = 10;
        var bin_width = (max - min)/bins;

        var tag_cloud = $('#tagcloud');

        var tag_list = $('<ul>').appendTo(tag_cloud);

        $.each(data, function(key, val) {
            var w = val[0];
            var bin = Math.max(Math.ceil( (w-min) / bin_width ), 3);
            var link = $('<a>').text(key).attr('href', val[1])
                .attr('class', 'weight' + Math.round(bin))
                .appendTo($('<li>').appendTo(tag_list));
        });

    });
});

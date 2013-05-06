.. link:
.. description:
.. tags: draft
.. date: 2013/04/17 21:16:53
.. title: About
.. slug: about


This site was started by a bunch of people, who fell in love with
Ultimate.  The idea is to have a site where we ramble about Ultimate,
and put up anything Ultimate.  We are hoping to have a lot of fun
here, while we share our experiences and tips & techniques to become
better Ultimate players.

If you wish to contribute, either send a pull request on `GitHub
<https://github.com/pankajp/ultimate-sport>`_ or leave a comment `here
</posts/welcome-to-ultimate-sport.html>`_.

.. raw:: html

    </a>

    <br>
    <div>Deployer status: <img id="deploy-status" src="/status.png" style="border-radius:10px;background-color:gray;padding:3px;width:50px;height:23px" alt="Checking..." ></div>
    <script>
    console.log(document.body);
    (function(){
        var elem = document.getElementById('deploy-status');
        elem.src = 'http://'+window.location.hostname+':8008/status.png';

        var gh_fork = document.createElement('a');
        gh_fork.href = "https://github.com/pankajp/ultimate-sport";
        gh_fork.innerHTML =  '<img style="position: absolute; right: 0; border: 0;" '+
                    'src="https://s3.amazonaws.com/github/ribbons/forkme_right_orange_ff7600.png" '+
                    'alt="Fork me on GitHub">';
        document.querySelector('.navbar.navbar-fixed-top').appendChild(gh_fork);
    })();
    </script>


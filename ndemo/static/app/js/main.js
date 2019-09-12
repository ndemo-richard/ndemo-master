/**
*------------------------------------------------------------------------------
* main.js
*-----------------------------------------------------------------------------
*/

(function($) {

        "use strict";

    /*----------------------- *.
    /* preloader
    -------------------------------------- */
    $(window).load(function() {

       //will first fade out the loading animation
       $("#loader").fadeOut("slow", function(){

        // will load out the whole DIV that covers the website
       $("#preloader").delay(300).fadeOut("slow");
       });

    })

    /*--------------------------------------------- */
    /* smooth scrolling
    -----------------------------------------------*/
    $('.smoothscroll').on('click', function (e) {

            e.preventDefault();

    var target = this.hash,
    $target = $(target);

    $('html, body').stop().animate({
    'scrollTop': $target.offset().top
    }, 800, 'swing', function () {
        window.location.hash = target;
    })
    })

    /*----------------------------------------- */
    /* back to top
    /*----------------------------------------- */
    var pxShow = 300; // height o n which the button will show
    var fadeInTime = 400; // how slow/fast you want the button to show
    var fadeOutTime = 400; //how slow/fast you want the button to hide
    var scrollSpeed = 300; // how slow/fast you want the button to scroll to top. can be a value, 'slow', 'normal' or 'fast'

    //sjow or hide the sticky footer button
    jQuery(window).scroll(function() {

            if (!( $("#header-search").hasClass('is-visible'))) {

                    if (jQuery(window).scrollTop() >= pxShow) {
                            jQuery("#go-top").fadeIn(fadeInTime);
                    } else {
                            jQuery("#go-top").fadeOut(fadeOutTime)
                    }
            }
    });

})(jQuery);


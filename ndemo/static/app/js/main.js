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
       $("#preloader").delay(5).fadeOut("slow");
       });

    })
     $("#owl-slider").owlCarousel({
     navigation: false,
     pagination: true,
     itemsCustom : [
	        [0, 1],
	        [700, 2],
	        [960, 3]
	     ],
        navigationText: false
    });

       /*----------------------------------------------------- */
	/* Alert Boxes
  	------------------------------------------------------- */
	$('.alert-box').on('click', '.close', function() {
	  $(this).parent().fadeOut(500);
	});

       /*---------------------------------------------------- */
	/*	Masonry
	------------------------------------------------------ */
	var containerProjects = $('#folio-wrapper');

	containerProjects.imagesLoaded( function() {

		containerProjects.masonry( {
		  	itemSelector: '.folio-item',
		  	resize: true
		});

	});


        	/*----------------------------------------------------*/
	/*	Modal Popup
	------------------------------------------------------*/
   $('.item-wrap a').magnificPopup({
      type:'inline',
      fixedContentPos: false,
      removalDelay: 300,
      showCloseBtn: false,
      mainClass: 'mfp-fade'

   });

   $(document).on('click', '.popup-modal-dismiss', function (e) {
   	e.preventDefault();
   	$.magnificPopup.close();
   });

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
    });

    /*---------------------------------------------------- */
	/*  Placeholder Plugin Settings
	------------------------------------------------------ */
	$('input, textarea, select').placeholder()


  	/*---------------------------------------------------- */
	/*	contact form
	------------------------------------------------------ */

	/* local validation */
	$('#contactForm').validate({

		/* submit via ajax */
		submitHandler: function(form) {

			var sLoader = $('#submit-loader');

			$.ajax({

		      type: "POST",
		      url: "inc/sendEmail.php",
		      data: $(form).serialize(),
		      beforeSend: function() {

		      	sLoader.fadeIn();

		      },
		      success: function(msg) {

	            // Message was sent
	            if (msg == 'OK') {
	            	sLoader.fadeOut();
	               $('#message-warning').hide();
	               $('#contactForm').fadeOut();
	               $('#message-success').fadeIn();
	            }
	            // There was an error
	            else {
	            	sLoader.fadeOut();
	               $('#message-warning').html(msg);
		            $('#message-warning').fadeIn();
	            }

		      },
		      error: function() {

		      	sLoader.fadeOut();
		      	$('#message-warning').html("Something went wrong. Please try again.");
		         $('#message-warning').fadeIn();

		      }

	      });
  		}

	});



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


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
    $(window).on('load',function() {

       //will first fade out the loading animation
       $("#loader").fadeOut("slow", function(){

        // will load out the whole DIV that covers the website
       $("#preloader").delay(1).fadeOut("slow");
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

	var token = '2024542625.1677ed0.30f58e666eab456ab0a7a5ac39949983',
    num_photos = 10,
    container = document.getElementById( 'instafeed' ),
    scrElement = document.createElement( 'script' );

window.mishaProcessResult = function( data ) {
	var x;
	for( x in data.data ){
		container.innerHTML += '<li><img src="' + data.data[x].images.low_resolution.url + '"></li>';
	}
}

scrElement.setAttribute( 'src', 'https://api.instagram.com/v1/users/self/media/recent?access_token=' + token + '&count=' + num_photos + '&callback=mishaProcessResult' );
document.body.appendChild( scrElement );

// const TypeWriter = function(txtElement, words, wait = 3000) {
//   this.txtElement = txtElement;
//   this.words = words;
//   this.txt = '';
//   this.wordIndex = 0;
//   this.wait = parseInt(wait, 10);
//   this.type();
//   this.isDeleting = false;
// }

// // Type Method
// TypeWriter.prototype.type = function() {
//   // Current index of word
//   const current = this.wordIndex % this.words.length;
//   // Get full text of current word
//   const fullTxt = this.words[current];

//   // Check if deleting
//   if(this.isDeleting) {
//     // Remove char
//     this.txt = fullTxt.substring(0, this.txt.length - 1);
//   } else {
//     // Add char
//     this.txt = fullTxt.substring(0, this.txt.length + 1);
//   }

//   // Insert txt into element
//   this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

//   // Initial Type Speed
//   let typeSpeed = 300;

//   if(this.isDeleting) {
//     typeSpeed /= 2;
//   }

//   // If word is complete
//   if(!this.isDeleting && this.txt === fullTxt) {
//     // Make pause at end
//     typeSpeed = this.wait;
//     // Set delete to true
//     this.isDeleting = true;
//   } else if(this.isDeleting && this.txt === '') {
//     this.isDeleting = false;
//     // Move to next word
//     this.wordIndex++;
//     // Pause before start typing
//     typeSpeed = 500;
//   }

//   setTimeout(() => this.type(), typeSpeed);
// }


// ES6 Class
class TypeWriter {
  constructor(txtElement, words, wait = 3000) {
    this.txtElement = txtElement;
    this.words = words;
    this.txt = '';
    this.wordIndex = 0;
    this.wait = parseInt(wait, 10);
    this.type();
    this.isDeleting = false;
  }

  type() {
    // Current index of word
    const current = this.wordIndex % this.words.length;
    // Get full text of current word
    const fullTxt = this.words[current];

    // Check if deleting
    if(this.isDeleting) {
      // Remove char
      this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
      // Add char
      this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    // Insert txt into element
    this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

    // Initial Type Speed
    let typeSpeed = 300;

    if(this.isDeleting) {
      typeSpeed /= 2;
    }

    // If word is complete
    if(!this.isDeleting && this.txt === fullTxt) {
      // Make pause at end
      typeSpeed = this.wait;
      // Set delete to true
      this.isDeleting = true;
    } else if(this.isDeleting && this.txt === '') {
      this.isDeleting = false;
      // Move to next word
      this.wordIndex++;
      // Pause before start typing
      typeSpeed = 500;
    }

    setTimeout(() => this.type(), typeSpeed);
  }
}


// Init On DOM Load
document.addEventListener('DOMContentLoaded', init);

// Init App
function init() {
  const txtElement = document.querySelector('.txt-type');
  const words = JSON.parse(txtElement.getAttribute('data-words'));
  const wait = txtElement.getAttribute('data-wait');
  // Init TypeWriter
  new TypeWriter(txtElement, words, wait);
}

})(jQuery);


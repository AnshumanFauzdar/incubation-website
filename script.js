$(window).on('load', function() { // makes sure the whole site is loaded
  $('#status').delay(3500).fadeOut(); // will first fade out the loading animation
  $('#preloader').delay(3500).fadeOut('slow'); // will fade out the white DIV that covers the website.
  $('body').delay(3600).css({'overflow':'visible'});
})

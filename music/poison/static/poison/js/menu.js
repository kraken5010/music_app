/* Responsive menu */
$(document).ready(function () {
  var touch = $('.touch-menu');
  var menu = $('.mainmenu');

  $(touch).on('click', function (e) {
    e.preventDefault();
    menu.slideToggle();
  });
  $(window).resize(function () {
    var wid = $(window).width();
    if (wid > 1000 && menu.is(':hidden')) {
      menu.removeAttr('style');
    }
  });
});
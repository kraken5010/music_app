// Главный слайдер
$(document).ready(function () {
  $('.bxslider').bxSlider({
    adaptiveHeight: false, // Отмена подстройки изображения под его высоту
    auto: true,
    infiniteLoop: false,
    hideControlOnEnd: true, // Круговая
    infiniteLoop: true,
    slideMargin: 0,
    pager: false,
    options: false, // Кнопи переключения
    prevText: "",
    nextText: "",
    pause: 6000 //Задержка слайда
  });
});

/* Фиксированная панель */
var h_hght = 915;// высота шапки
var h_mrg = 0;    // отступ когда шапка уже не видна
$(function () {
  $(window).scroll(function () {
    var top = $(this).scrollTop();
    var elem = $('.top-panel');
    if (top + h_mrg < h_hght) {
      elem.css('top', (h_hght - top));
    } else {
      elem.css('top', h_mrg);
      elem.css('margin', 0);
    }
  });
});

// Слайдер NEWS
$(document).ready(function () {
  $('.slider4').bxSlider({
    slideWidth: 370,
    minSlides: 1,
    maxSlides: 4,
    moveSlides: 1,
    slideMargin: 30,
    pager: false,
    options: true,
  });
});

/* Responsive menu */
$(document).ready(function () {
  var touch = $('.touch-menu');
  var menu = $('.menu');

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


// Параллакс
$(document).ready(function () {
  $("section[data-type='background']").each(function () {
    var $bgobj = $(this);

    $(window).scroll(function () {
      var yPos = -($(window).scrollTop() / $bgobj.data("speed"));
      var coords = "50%" + yPos + "px";
      $bgobj.css("background-position", coords);
    });
  });
});


// Слайдер с текстом
$(document).ready(function () {
  $('.slide-text').bxSlider({
    hideControlOnEnd: true,
    adaptiveHeight: false, // Отмена подстройки изображения под его высоту
    hideControlOnEnd: true, // Круговая
    infiniteLoop: true,
    slideMargin: 0,
    pager: true,
    options: false, // Кнопи переключения
    prevText: "",
    nextText: "",
    controls: false
  });
});


// Слайдер блока BAND 
$(document).ready(function () {
  $('.slider1').bxSlider({
    slideWidth: 370,
    minSlides: 1,
    maxSlides: 4,
    slideMargin: 30,
    pager: false,
    moveSlides: 1,
    infiniteLoop: false,
  });
});
//general
var windowHeight = $(window).height();
var getURL = window.location.href;

// in login
if (getURL.includes('login')) {
    $(".navbar-brand").css("display", "none");
    $(".about").css("display", "none");
}

// in index and profile for tooltip
$(function() {
    $('[data-toggle="tooltip"]').tooltip()
})

// in register
if (getURL.includes('register')) {
    $(".navbar-brand").css("display", "none");
    $(".about").css("display", "none");
}

// create meme
setTimeout(function() {
    $('.notMeme').fadeOut('fast');
}, 5000);
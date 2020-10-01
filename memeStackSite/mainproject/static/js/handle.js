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

// bg in login & reg
if (getURL.includes('login') || getURL.includes('register')) {
    $(".mainContainer").addClass("bg_wallpaper");
    $(".bg_wallpaper").css("height", windowHeight);
    $(".navbar").css("background", "rgba(0,0,0,0.5)");
    $(".navbar").removeClass("bg-light");
} else {
    $(".mainContainer").removeClass("bg_wallpaper");
}
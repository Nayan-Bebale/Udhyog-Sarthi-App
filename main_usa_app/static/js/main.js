// Font size increase and decrease
// Default font size in pixels
const DEFAULT_FONT_SIZE = 16; // Adjust this to match your default font size

// Function to change font size
function changeFontSize(step) {
    const htmlElement = document.documentElement;
    const currentSize = parseFloat(window.getComputedStyle(htmlElement).fontSize);
    const newSize = currentSize + step;
    htmlElement.style.fontSize = `${newSize}px`;
}

// Function to reset font size to default
function resetFontSize() {
    document.documentElement.style.fontSize = `${DEFAULT_FONT_SIZE}px`;
}

// Event listeners for buttons
document.getElementById('increase-font-size').addEventListener('click', () => {
    changeFontSize(2); // Increase font size by 2px
});

document.getElementById('decrease-font-size').addEventListener('click', () => {
    changeFontSize(-2); // Decrease font size by 2px
});

document.getElementById('reset-font-size').addEventListener('click', () => {
    resetFontSize(); // Reset font size to default
});



document.getElementById('theme-selector').addEventListener('change', function() {
    const selectedTheme = this.value;
  
    switch (selectedTheme) {
        case 'theme1':
            setThemeVariables('#00B98E', '#FF6922', '#EFFDF5', '#0E2E50'); // High Contrast Black & White
            break;  
        case 'theme2':
            setThemeVariables('#FFFFFF', '#000000', '#000000', '#FFFFFF'); // High Contrast White & Black
            break;
        case 'theme3':
            setThemeVariables('#1E90FF', '#FFD700', '#F0F8FF', '#00008B'); // High Contrast Blue & Gold
            break;
        case 'theme4':
            setThemeVariables('#8B0000', '#FFA07A', '#FFE4E1', '#8B0000'); // High Contrast Red & Light Coral
            break;
        case 'theme5':
            setThemeVariables('#006400', '#ADFF2F', '#F0FFF0', '#006400'); // High Contrast Green & Green Yellow
            break;
    }
});


function setThemeVariables(primaryColor, secondaryColor, lightColor, darkColor) {
    document.documentElement.style.setProperty('--primary', primaryColor);
    document.documentElement.style.setProperty('--secondary', secondaryColor);
    document.documentElement.style.setProperty('--light', lightColor);
    document.documentElement.style.setProperty('--dark', darkColor);
}

(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.nav-bar').addClass('sticky-top');
        } else {
            $('.nav-bar').removeClass('sticky-top');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });
    
})(jQuery);


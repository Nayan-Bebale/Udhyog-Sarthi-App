document.getElementById('theme-selector').addEventListener('change', function() {
    const selectedTheme = this.value;
  
    switch (selectedTheme) {
        case 'theme1':
            setThemeVariables('#00B98E', '#FF6922', '#EFFDF5');
            break;  
        case 'theme2':
            setThemeVariables('#3498db', '#f1c40f', '#f9f9f9');
            break;
        case 'theme3':
            setThemeVariables('#2ecc71', '#9b59b6', '#e5e5e5');
            break;
        case 'theme4':
            setThemeVariables('#e74c3c', '#2c3e50', '#ccc');
        // case 'custom':
        //     setThemeVariables('#030637', '#3C0753', '#720455', '#910A67');
        //     break;
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


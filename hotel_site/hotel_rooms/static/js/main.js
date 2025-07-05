'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    //Offcanvas Menu
    $(".canvas-open").on('click', function () {
        $(".offcanvas-menu-wrapper").addClass("show-offcanvas-menu-wrapper");
        $(".offcanvas-menu-overlay").addClass("active");
    });

    $(".canvas-close, .offcanvas-menu-overlay").on('click', function () {
        $(".offcanvas-menu-wrapper").removeClass("show-offcanvas-menu-wrapper");
        $(".offcanvas-menu-overlay").removeClass("active");
    });

    // Search model
    $('.search-switch').on('click', function () {
        $('.search-model').fadeIn(400);
    });

    $('.search-close-switch').on('click', function () {
        $('.search-model').fadeOut(400, function () {
            $('#search-input').val('');
        });
    });

    /*------------------
        Navigation
    --------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*------------------
        Hero Slider
    --------------------*/
    $(".hero-slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: true,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        mouseDrag: false
    });

    /*------------------------
        Testimonial Slider
    ----------------------- */
    $(".testimonial-slider").owlCarousel({
        items: 1,
        dots: false,
        autoplay: true,
        loop: true,
        smartSpeed: 1200,
        nav: true,
        navText: ["<i class='arrow_left'></i>", "<i class='arrow_right'></i>"]
    });

    /*------------------
        Magnific Popup
    --------------------*/
    $('.video-popup').magnificPopup({
        type: 'iframe'
    });

    /*------------------
        Date Picker
    --------------------*/
    $(".date-input").datepicker({
        minDate: 0,
        dateFormat: 'dd MM, yy'
    });

    /*------------------
        Nice Select
    --------------------*/
    $("select").niceSelect();

    var $cur_date = new Date().toISOString().slice(0, 10)
    $('.date-in').attr({
        'min': $cur_date,
    })

    $('.date-in').change(function () {
        let selected_date = new Date($(this).val())
        selected_date.setDate(selected_date.getDate() + 1)
        let date = selected_date.toISOString().slice(0, 10)
        $('.date-out').attr({
            'min': date,
            'value': date
        })
    })

    var $tomorrow_date = new Date(new Date().getTime() + 24 * 60 * 60 * 1000).toISOString().slice(0, 10)
    $('.date-out').attr({
        'min': $tomorrow_date,
    })
    $("form button[type=submit]").click(function () {
        if ($('.guests').val()) {
            sessionStorage.setItem('guests', $('.guests').val())
        }
        if ($('.date-out').val()) {
            sessionStorage.setItem("dateOut", $(".date-out").val())
        }
        if ($('.date-in').val()) {
            sessionStorage.setItem("dateIn", $(".date-in").val())
        }
    })

    
    $( "#slider-range" ).slider({
        range: true,
        min: 100,
        max: 500,
        values: [ 100, 500 ],
        slide: function( event, ui ) {
        $( "#amount" ).val( ui.values[ 0 ] + " Руб." + " - " + ui.values[ 1 ] + " Руб." );
        }
    });

    $( "#amount" ).val( $( "#slider-range" ).slider( "values", 0 ) + " Руб." + " - " +
        $( "#slider-range" ).slider( "values", 1 ) + " Руб." );

})(jQuery);
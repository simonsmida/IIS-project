/*!
* Start Bootstrap - Scrolling Nav v5.0.5 (https://startbootstrap.com/template/scrolling-nav)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-scrolling-nav/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});


/* Set select option to the default value */
$(document).ready(function () {
    $('#dates').val('default');
    $('#time').val('default');
});

$(document).ready(function () {
    // remove duplicate dates
    $("#dates option").each(function () {
        $(this).siblings("[value='" + this.value + "']").remove();
    }); 

    /* filter time options according to selected date */
    $('#dates').change(function () {
        var sel_date = $(this).find(":selected").val();
        $("#time").find("option").each(function () {
            if ($(this).val().includes(sel_date)) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });

    /* if time selected and date chaged, set time to default */
    $('#dates').change(function () {
        $('#time').val('default');
    });

    // today in yyyy-mm-dd format
    var today = new Date().toISOString().slice(0, 10);
    $("#dates option").each(function () {
        var date = $(this).val();
        if (date < today) {
            $(this).hide();
        }
    });

    // if dates contains only default option, show message
    if ($('#dates option').length == 1) {
        // change text of the default option with red color
        $('#dates option').text('No available dates');
        $('#dates').css('color', 'red');
        // hide time select and label
        $('#time').hide();
        $('#time-label').hide();
        // hide submit button
        $('#reserve-btn').hide();
    } else {
        $('#time').show();
        $('#time-label').show();
    }
});


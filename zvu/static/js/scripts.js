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

/**
 * Caregiver side bar 
 */
// $(document).ready(function () {
//     $('#sidebar > ul > li').click(function() {
//         //1. Remove currently active class
//         $('#sidebar > ul > li.active').removeClass('active');

//         //2. Set new active class to the currently clicked object
//         var index = $(this).index();
//         $("#sidebar > ul > li:nth-child("+(index+1)+")").addClass('active');
//     });
// });

/**
 * Verify volunteer -> ajax
 */
 $(document).ready(function () {
    $(document).on("click","button.verify", function(){
        //1. Remove currently active class
        console.log('You clicked button for verification');
        var id = $(this).attr("id");
        console.log(id);
        $.ajax({
            type: 'GET',
            url: '/caregiver/manage_volunteers/verify',
            data: {
                "id" : id
            },
            success: function( data ){
                console.log(data);
                $('.volunteer-wrap').empty();
                $('.volunteer-wrap').html(data);
            },
            error: function(){
                console.log("Error bad response");
            }

        });
    });

});


/**
 * Unverify volunteer -> ajax
 */
$(document).ready(function () {
    $(document).on("click","button.unverify", function(){
        //1. Remove currently active class
        console.log('You clicked button for unverification');
        var id = $(this).attr("id");
        console.log(id);
        $.ajax({
            type: 'GET',
            url: '/caregiver/manage_volunteers/unverify',
            data: {
                "id" : id
            },
            success: function( data ){
                console.log(data);
                $('.volunteer-wrap').empty();
                $('.volunteer-wrap').html(data);
            },
            error: function(){
                console.log("Error bad response");
            }

        });
    });

});

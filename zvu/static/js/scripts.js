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

/**
 * APPROVE RESERVATIONS
 */

/**
 * Function for filtering reservations 
 */
 $(document).ready(function () {
    $(document).on("click","button.approve-res-date", function(){
        // 1. Get data from input fields
        var from = $('#startDateApprove').val();
        var to = $('#endDateApprove').val();
        var approval_type = $('#approve-type').val();
        var dateFrom = new Date(from);
        var dateTo = new Date(to);
        // 2. Check if the input dates are valid 
        if (dateFrom > dateTo){
            $(".approve-result").html("<p> No reservations in selected date</p>");
            console.log("error");
        }else{
            console.log('Sending to server...');
            console.log(dateFrom);
            console.log(dateTo);
            console.log(from);
            console.log(to);
            console.log(approval_type);
            $.ajax({
            type: 'GET',
            url: '/caregiver/approve_res/get_reservations',
            data: {
                "from" : from,
                "to" : to,
                "approval_type": approval_type
            },
            success: function( data ){
                console.log(data);
                $('.approve-result').empty();
                $('.approve-result').html(data);
            },
            error: function(){
                console.log("Error bad response");
            }

        });

        }
    });
});

/**
 * Function for approving reservations
 */
$(document).ready(function () {
    $(document).on("click","button.change-approvement", function(){
        //1. Remove currently active class
        console.log('You clicked button changing approvement');
        var id = $(this).attr("res-id");
        var approve = $(this).attr("approve");
        var from = $('#startDateApprove').val();
        var to = $('#endDateApprove').val();
        var approval_type = $('#approve-type').val();
        console.log(id);
        console.log(approve);
        $.ajax({
            type: 'GET',
            url: '/caregiver/approve_res/approve',
            data: {
                "from" : from,
                "to" : to,
                "approval_type": approval_type,
                "id" : id,
                "approve" : approve
            },
            success: function( data ){
                console.log(data);
                $('.approve-result').empty();
                $('.approve-result').html(data);
            },
            error: function(){
                console.log("Error bad response");
            }

        });
    });

});
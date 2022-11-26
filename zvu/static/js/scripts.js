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

/**
 * REGISTER WALKS
 */

/**
 * Function for displaying time edit
 */
 $(document).ready(function () {
    $(document).on("click","button.walk-time-edit", function(){
        //1. Remove currently active class
        console.log('You clicked button for editing walk time');
        var id = $(this).attr("editrow-id");
        var row_id = "#set-time-"+id+".walk-new-time";
        var visibility = $(row_id).attr("style");
        console.log(id);
        console.log(visibility);
        console.log(row_id);
        if (visibility === "display:none"){
            $(row_id).attr("style","display:table-row");
        }
        else if(visibility === "display:table-row"){
            $(row_id).attr("style","display:none");
        }

    });

});

/**
 * Function for saving walk times
 */
$(document).ready(function () {
    $(document).on("click","button.walk-time-save", function(){
        //1. Remove currently active class
        console.log('You clicked button for saving walk time');
        var id = $(this).attr("settime-id");
        var time_picked = $("#walkStartTime-"+id).val()
        var time_return = $("#walkEndTime-"+id).val()

        console.log(id);
        console.log(time_picked);
        console.log(time_return);
        // if (time_picked > time_return) {
        //     console.log('Invalid time of return');
        // } 
        // else{
            $.ajax({
                type: 'GET',
                url: '/caregiver/register_walks/save',
                data: {
                    "id" : id,
                    "time_picked" : time_picked,
                    "time_return" : time_return,
                },
                success: function( data ){
                    console.log(data);
                    $('.walk-table').empty();
                    $('.walk-table').html(data);
                },
                error: function(){
                    console.log("Error bad response");
                }
            });
        // }
        
    });

});

// CAEEGIVER ANIMAL EDIT 
/**
 * Function for creating animals
 */
 $(document).ready(function () {
    $(document).on("click","button.create-animal", function(){
        //1. Remove currently active class
        console.log('You clicked button for creating animal');
        $.ajax({
            type: 'GET',
            url: '/caregiver/edit_animals/create_form',
            success: function( data ){
                console.log(data);
                $('.edit-animals-content').empty();
                $('.edit-animals-content').html(data);
            },
            error: function(){
                console.log("Error bad response");
            }
        });
    });

});

/**
 * Function for updating animals
 */
 $(document).ready(function () {
    $(document).on("click","button.update-animal", function(){
        //1. Get animal id
        var animal_id = $(this).attr("animal-id");
        var form_url = '/caregiver/edit_animals/'+animal_id+'/update';

        console.log(animal_id);
        console.log(form_url);
        console.log('You clicked button for updating animal');
        
        $.ajax({
            type: 'GET',
            url: '/caregiver/edit_animals/'+animal_id+'/update',
            success: function( data ){
                console.log(data);
                $('.edit-animals-content').empty();
                $('.edit-animals-content').html(data);
            },
            error: function(){
                console.log("Error bad response");
            }
        });
    });

});

/**
 * Function for deleting animals
 */
 $(document).ready(function () {
    $(document).on("click","button.delete-animal", function(){
        //1. Remove currently active class
        console.log('You clicked button for deleting animal');
        var animal_id = $(this).attr("animal-id");
        if(!confirm("Are you sure you want to delete an animal?")){
            return false;
        };
        console.log(animal_id);

        $.ajax({
            type: 'GET',
            url: '/caregiver/edit_animals/delete',
            data: {
                "id":animal_id
            },
            success: function( data ){
                console.log(data);
                $('.edit-animals-content').empty();
                $('.edit-animals-content').html(data);
            },
            error: function(){
                console.log("Error bad response");
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



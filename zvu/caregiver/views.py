from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from shelter.models import Reservation
from .decorators import user_group
from datetime import datetime


# Create your views here.
@login_required(login_url="login")
#@user_passes_test(lambda u: u.groups.filter(name='caregiver').exists(), login_url='../shelter/forbidden.html')
# @permission_required(perm='shelter.view_animal', raise_exception=True)
def caregiver_view(request):
    user = request.user
    if user.groups.filter(name='caregiver').exists() or user.is_superuser:
        #exists
        context = {
            "usr" : user
        }
        return render(request, "caregiver/caregiver.html", context)
    # raise PermissionDenied
    return HttpResponseForbidden()


@login_required(login_url="login")

@user_group('caregiver')
def manage_volunteers_view(request):
    #Get volunteers
    verified =  User.objects.filter(groups__name='volunteer')
    not_verified = User.objects.filter(groups__name='volunteer_notrust')
    context = {
        "verified": verified,
        "nonverified": not_verified,
        "content" : "manage_volunteers"
    }
    return render(request, "caregiver/caregiver.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def verify_volunteers_view(request):
    if request.method == "GET":
        print("I am going to verify ")
        # 1. Get user with specified ID
        volunteer_id = request.GET['id']
        volunteer_obj =  User.objects.get(id=volunteer_id)
        # 2. Get verified user group
        noverif_group = Group.objects.get(name="volunteer_notrust")
        verif_group = Group.objects.get(name="volunteer")
        if volunteer_obj != None:
            print(volunteer_obj.first_name)
            verif_group.user_set.add(volunteer_obj)
            noverif_group.user_set.remove(volunteer_obj)
            
            verified =  User.objects.filter(groups__name='volunteer')
            not_verified = User.objects.filter(groups__name='volunteer_notrust')
            context = {
                "verified": verified,
                "nonverified": not_verified,
                "content" : "manage_volunteers"
            }
            return render(request, "caregiver/manage_volunteers.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def unverify_volunteers_view(request):
    if request.method == "GET":
        print("I am going to unverify ")
        # 1. Get user with specified ID
        volunteer_id = request.GET['id']
        volunteer_obj =  User.objects.get(id=volunteer_id)
        # 2. Get user group
        noverif_group = Group.objects.get(name="volunteer_notrust")
        verif_group = Group.objects.get(name="volunteer")
        if volunteer_obj != None:
            print(volunteer_obj.first_name)
            verif_group.user_set.remove(volunteer_obj)
            noverif_group.user_set.add(volunteer_obj)
            
            verified =  User.objects.filter(groups__name='volunteer')
            not_verified = User.objects.filter(groups__name='volunteer_notrust')
            context = {
                "verified": verified,
                "nonverified": not_verified,
                "content" : "manage_volunteers"
            }
            return render(request, "caregiver/manage_volunteers.html", context)


@login_required(login_url="login")
@user_group('caregiver')

def edit_animals_view(request):
    context = {
        "content" : "edit_animals"
    }
    return render(request, "caregiver/caregiver.html", context)

@login_required(login_url="login")
@user_group('caregiver','volunteer')
def create_schedules_view(request):
    context = {
        "content" : "create_schedules"
    }
    return render(request, "caregiver/caregiver.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def approve_res_view(request):
    '''
    Returns view for approving reservations
    by caretaker
    '''
    reservations = Reservation.objects.all()
    context = {
        "content" : "approve_res",
        "reservations" : reservations
    }
    return render(request, "caregiver/caregiver.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def get_reservations(request):
    '''
    View for getting the reservation according to filter
    requirements sent from ajax request
    '''
    if request.method == "GET":
        from_date = request.GET['from']
        to_date = request.GET['to']
        approve = int(request.GET['approval_type'])
        print(from_date)
        print(to_date)
        print(approve)
        # 1. Filter according to date 
        if from_date == "" and to_date == "":
            reservations = Reservation.objects.all()
        elif from_date == "":
            reservations = Reservation.objects.filter(reserved_date__lt=to_date)
        elif to_date == "":
            reservations = Reservation.objects.filter(reserved_date__gt=from_date)
        else:
            reservations = Reservation.objects.filter(reserved_date__range=[from_date, to_date])
        
        # 2. Filter according to reservation approve 
        if approve == 0 or approve == 1:
            reservations = reservations.filter(approval__icontains=approve)
    context = {
        "reservations" : reservations
    }
    return render(request, "caregiver/approve_reservations.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def approve_reservation(request):
    '''
    Function changes approval field of the specified 
    reservation, according to id sent in request
    '''
    if request.method == "GET":
        approve = int(request.GET['approve'])
        res_id = int(request.GET['id'])
        Reservation.objects.filter(id=res_id).update(approval=approve)
        
        # reservation = Reservation.objects.get(id=res_id)
        # reservation.approval = approve
        # reservation.save()
        # To not clear current filter on page, we pass
        # filter data to get_reservations
        response = get_reservations(request)
        return response

@login_required(login_url="login")
@user_group('caregiver')
def register_walks_view(request):
    reservations = Reservation.objects.all()
    print(reservations)
    context = {
        "content" : "register_walks",
        "reservations" : reservations
    }
    return render(request, "caregiver/caregiver.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def save_walk_time(request):
    if request.method == "GET":
        # 1. Get values from request
        res_id = int(request.GET['id'])
        time_picked = request.GET['time_picked']
        time_return = request.GET['time_return']
        print(time_picked)
        print(time_return)
        print(type(time_return))
        # 3. Set new values from request
        if time_picked == "" and time_return == "":
            Reservation.objects.filter(id=res_id).update(time_picked=None, time_return=None)
        elif time_picked == "":
            Reservation.objects.filter(id=res_id).update(time_picked=None,time_return=time_return)
        elif time_return == "":
            Reservation.objects.filter(id=res_id).update(time_picked=time_picked,time_return=None)
        else:
            Reservation.objects.filter(id=res_id).update(time_picked=time_picked,time_return=time_return)
            
        reservations = Reservation.objects.all()
        context = {
            "reservations" : reservations
        }
        return render(request, "caregiver/walks_register.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def create_vet_request_view(request):
    context = {
        "content" : "create_vet_request"
    }
    return render(request, "caregiver/caregiver.html", context)

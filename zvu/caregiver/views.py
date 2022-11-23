from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .decorators import user_group

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
@user_group('caregiver','volunteer')
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
@user_group('caregiver','volunteer')
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
@user_group('caregiver','volunteer')
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
@user_group('caregiver','volunteer')
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
@user_group('caregiver','volunteer')
def register_walks_view(request):
    context = {
        "content" : "register_walks"
    }
    return render(request, "caregiver/caregiver.html", context)

@login_required(login_url="login")
@user_group('caregiver','volunteer')
def create_vet_request_view(request):
    context = {
        "content" : "create_vet_request"
    }
    return render(request, "caregiver/caregiver.html", context)

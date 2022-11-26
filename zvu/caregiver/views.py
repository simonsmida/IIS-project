from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from shelter.models import Reservation, Animal
from .decorators import user_group
from datetime import datetime
from animals.forms import AnimalForm
from timetable.forms import TimetableForm2
from shelter.models import Timetable

# Create your views here.
@login_required(login_url="login")
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
        # 1. Get user with specified ID
        volunteer_id = request.GET['id']
        volunteer_obj =  User.objects.get(id=volunteer_id)
        # 2. Get verified user group
        noverif_group = Group.objects.get(name="volunteer_notrust")
        verif_group = Group.objects.get(name="volunteer")
        if volunteer_obj != None:
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
        # 1. Get user with specified ID
        volunteer_id = request.GET['id']
        volunteer_obj =  User.objects.get(id=volunteer_id)
        # 2. Get user group
        noverif_group = Group.objects.get(name="volunteer_notrust")
        verif_group = Group.objects.get(name="volunteer")
        if volunteer_obj != None:
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
    animals = Animal.objects.all()
    context = {
        "content" : "edit_animals",
        "animals" : animals
    }
    return render(request, "caregiver/caregiver.html", context)


#################################
###     SCHEDULE CREATION     ###
#################################

@login_required(login_url="login")
@user_group('caregiver','volunteer')
def create_schedules_view(request):
    animals = Animal.objects.all()
    context = {
        "content" : "create_schedules",
        "animals" : animals
    }
    return render(request, "caregiver/caregiver.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def animal_schedules_list(request, myid=id):
    animal = Animal.objects.get(id=myid)
    timetables = Timetable.objects.filter(animalid=myid)
    context = {
        "content" : "create_schedules",
        "animal" : animal,
        "timetables" : timetables,
        "animal_list": "yes", 
    }
    return render(request, "caregiver/caregiver.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def schedule_update_time(request, myid=id):
    if request.method == "GET":
        # 1. Get values from request
        timetable_id = int(request.GET['tableid'])
        date = request.GET['date']
        time_from = request.GET['time_from']
        time_to = request.GET['time_to']
        
        #Set date
        if date == "":
            Timetable.objects.filter(id=timetable_id).update(reserved_date=None)
        else:
            Timetable.objects.filter(id=timetable_id).update(reserved_date=date)
        
        #Set time from
        if time_from == "":
            Timetable.objects.filter(id=timetable_id).update(reserved_from=None)
        else:
            Timetable.objects.filter(id=timetable_id).update(reserved_from=time_from)
            
        #Set time to
        if time_to == "":
            Timetable.objects.filter(id=timetable_id).update(reserved_to=None)
        else:
            Timetable.objects.filter(id=timetable_id).update(reserved_to=time_to)            
        
        animal = Animal.objects.get(id=myid)
        timetables = Timetable.objects.filter(animalid=myid)
        context = {
            "content" : "create_schedules",
            "animal" : animal,
            "timetables" : timetables,
        }
        return render(request, "caregiver/schedules_animal.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def schedule_create_form(request):
    if request.method == "GET":
        animal_id = request.GET["id"]
        form = TimetableForm2()     
        context = {
            'form': form,
            'animal_id': animal_id
        }
        return render(request, "caregiver/schedule_form_create.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def schedule_create(request, myid=id):
    if request.method == "POST":
        animal = Animal.objects.get(id=myid)
        form = TimetableForm2(request.POST, instance=animal)     
        if form.is_valid():
            reserved_date = form.cleaned_data['reserved_date']
            reserved_from = form.cleaned_data['reserved_from']
            reserved_to = form.cleaned_data['reserved_to']
            timetable = Timetable(reserved_date=reserved_date,
                                  reserved_from=reserved_from,
                                  reserved_to=reserved_to,
                                  animalid=animal)
            timetable.save()
        return redirect(f"/caregiver/create_schedules/animal_schedules/{myid}/")

@login_required(login_url="login")
@user_group('caregiver')
def schedule_delete_time(request, myid=id):
    if request.method == "GET":
        timetable_id = request.GET["id"]
        delete_animal = Timetable.objects.get(id=timetable_id)
        delete_animal.delete()
        animal = Animal.objects.get(id=myid)
        timetables = Timetable.objects.filter(animalid=myid)
        context = {
            "content" : "create_schedules",
            "animal" : animal,
            "timetables" : timetables,
        }
        return render(request, "caregiver/schedules_animal.html", context)

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
        response = get_reservations(request)
        return response

@login_required(login_url="login")
@user_group('caregiver')
def register_walks_view(request):
    reservations = Reservation.objects.all()
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
        # 3. Set new values from request
        if time_picked == "" and time_return == "":
            Reservation.objects.filter(id=res_id).update(time_picked=None, time_return=None)
            Reservation.objects.filter(id=res_id).update(state="Pending")
        elif time_picked == "":
            Reservation.objects.filter(id=res_id).update(time_picked=None,time_return=time_return)
            Reservation.objects.filter(id=res_id).update(state="Finished")
        elif time_return == "":
            Reservation.objects.filter(id=res_id).update(time_picked=time_picked,time_return=None)
            Reservation.objects.filter(id=res_id).update(state="Pending")
        else:
            Reservation.objects.filter(id=res_id).update(state="Finished")
            Reservation.objects.filter(id=res_id).update(time_picked=time_picked,time_return=time_return)
            Reservation.objects.filter(id=res_id).update(state="Finished")
            
            
        reservations = Reservation.objects.all()
        context = {
            "reservations" : reservations
        }
        return render(request, "caregiver/walks_register.html", context)


@login_required(login_url="login")
@user_group('caregiver')
def animal_create_form_view(request):
    form = AnimalForm()     
    context = {
        'form': form,
    }
    return render(request, "caregiver/edit_animal_create.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def animal_create_view(request):
    form = AnimalForm(request.POST or None)     
    if form.is_valid():
        form.save()
        form = AnimalForm()
    return redirect("/caregiver/edit_animals/")


@login_required(login_url="login")
@user_group('caregiver')
def animal_update_view(request, id=id):
    obj = get_object_or_404(Animal, id=id)
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=obj)     
        if form.is_valid():
            form.save()
        return redirect("/caregiver/edit_animals/")
    else:
        form = AnimalForm(instance=obj)     
    context = {"form":form, "id": id}
    return render(request, "caregiver/edit_animal_update.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def animal_delete_view(request):
    if request.method == "GET":
        animal_id = request.GET["id"]
        delete_animal = Animal.objects.get(id=animal_id)
        delete_animal.delete()
        animals = Animal.objects.all()
        context = {"animals":animals}
        return render(request, "caregiver/edit_animals.html", context)

@login_required(login_url="login")
@user_group('caregiver')
def create_vet_request_view(request):
    context = {
        "content" : "create_vet_request"
    }
    return render(request, "caregiver/caregiver.html", context)

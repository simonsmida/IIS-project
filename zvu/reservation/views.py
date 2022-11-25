from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReservationForm, ReservationManageForm, ReservationUpdateForm
from shelter.models import Reservation, Animal
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponseForbidden   
from animals.templatetags.animals_extras import has_group
from reservation.decorators import my_login_required


@my_login_required
@permission_required("shelter.add_reservation", login_url="login", raise_exception=True)
def reservation_create_view(request):
    form = ReservationForm(request.POST or None)
    if request.user.is_superuser:
        # zviera = ""
        form = ReservationManageForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('../')
    # else:
        # zviera = "Reservation for "
    if form.is_valid():
        reservation = form.save(commit=False)
        reservation.volunteerid = request.user
        reservation.save()
        return redirect('../')
    
    # zviera = f"{zviera} \"{request.POST.get('zviera', False)}\"" 
    context = {
        'form': form,
        # 'zviera': zviera
    }
    return render(request, "reservation/reservation_create.html", context)


@login_required(login_url="login")
@permission_required("shelter.change_reservation", login_url="login", raise_exception=True)
def reservation_update_view(request, id=id):
    user = request.user
    obj = get_object_or_404(Reservation, id=id)
    
    if obj.volunteerid == user or user.is_superuser or has_group(request.user, 'caregiver'):
        form = ReservationUpdateForm(request.POST or None, instance=obj)
        
        if user.is_superuser or has_group(request.user, 'caregiver'):
            form = ReservationManageForm(request.POST or None, instance=obj)
            
        if form.is_valid():
            form.save()
            return redirect('../../')
        
        context = {
            'form': form
        }
        return render(request, "reservation/reservation_create.html", context)
    return HttpResponseForbidden()
    

@login_required(login_url="login")
@permission_required("shelter.view_reservation", login_url="login", raise_exception=True)
def reservation_list_view(request):
    queryset1 = Reservation.objects.filter(volunteerid=request.user) # list of objects
    queryset2 = []
    if request.user.is_superuser or has_group(request.user, 'caregiver'):
        queryset1 = Reservation.objects.filter(approval=0) # list of objects
        queryset2 = Reservation.objects.filter(approval=1)
        queryset2 = queryset2.order_by('animalid')
        
    queryset1 = queryset1.order_by('animalid')
    
    context = {
        "object_list1": queryset1,
        "object_list2": queryset2   
    }
    return render(request, "reservation/reservation_list.html", context)


@login_required(login_url="login")
@permission_required("shelter.view_reservation", login_url="login", raise_exception=True)
def reservation_detail_view(request, id):
    obj = get_object_or_404(Reservation, id=id)
    if obj.volunteerid == request.user or request.user.is_superuser or has_group(request.user, 'caregiver'):
        context = {
            "object": obj
        }
        return render(request, "reservation/reservation_detail.html", context)
    return HttpResponseForbidden()


@login_required(login_url="login")
@permission_required("shelter.delete_reservation", login_url="login", raise_exception=True)
def reservation_delete_view(request, id):
    obj = get_object_or_404(Reservation, id=id)
    if obj.volunteerid == request.user or request.user.is_superuser or has_group(request.user, 'caregiver'):
        if request.method == "POST":
            obj.delete()
            return redirect('../../')
        context = {
            "object": obj
        }
        return render(request, "reservation/reservation_delete.html", context)
    return HttpResponseForbidden()
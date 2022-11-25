from django.shortcuts import render, get_object_or_404, redirect
from .forms import TimetableForm
from shelter.models import Timetable, Animal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from caregiver.decorators import user_group


@login_required(login_url="login")
@user_group('caregiver')
def timetable_create_view(request):
    form = TimetableForm(request.POST or None)
    if form.is_valid():
        animalid = form.cleaned_data["animalid"]
        form.save()
        return redirect(f'../../animals/{animalid.id}')
    context = { 
        'form': form
    }
    return render(request, "timetable/timetable_create.html", context)


@login_required(login_url="login")
@user_group('caregiver')
def timetable_update_view(request, id=id):
    obj = get_object_or_404(Timetable, id=id)
    form = TimetableForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(f'../../../animals/{obj.animalid.id}')
    context = {
        'form': form
    }
    return render(request, "timetable/timetable_create.html", context)


@login_required(login_url="login")
def timetable_list_view(request):
    queryset1 = []
    if request.POST.get('animalid', False):
        animalid = request.POST['animalid']
    # animal = get_object_or_404(Animal, id=animalid)
    # animal_name = animal.name
        queryset = Timetable.objects.filter(animalid=animalid)# list of objects
        queryset1 = queryset.order_by('reserved_from','reserved_to')

    context = {
        "object_list1": queryset1,
        # "animal_name": animal_name,
    }
    return render(request, "timetable/timetable_list.html", context)


@login_required(login_url="login")
@user_group('caregiver')
def timetable_delete_view(request, id):
    obj = get_object_or_404(Timetable, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect(f'../../../animals/{obj.animalid.id}')
    context = {
        "object": obj
    }
    return render(request, "timetable/timetable_delete.html", context)

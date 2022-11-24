from django.shortcuts import render, get_object_or_404, redirect
from .forms import TimetableForm
from shelter.models import Timetable
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
        return redirect("animals:animal-detail")
    context = {
        'form': form
    }
    return render(request, "timetable/timetable_create.html", context)


@login_required(login_url="login")
def timetable_list_view(request):
    if request.POST.get('animalid', False):
        animalid = request.POST['animalid']
    queryset = Timetable.objects.filter(animalid=animalid)# list of objects
    queryset1 = queryset.order_by('reserved_from','reserved_to')
    # queryset1 = queryset.filter(day='Pondelok')
    # queryset2 = queryset.filter(day='Utorok')
    # queryset3 = queryset.filter(day='Streda')
    # queryset4 = queryset.filter(day='Stvrtok')
    # queryset5 = queryset.filter(day='Piatok')
    context = {
        "object_list1": queryset1,
        # "object_list2": queryset2,
        # "object_list3": queryset3,
        # "object_list4": queryset4,
        # "object_list5": queryset5
    }
    return render(request, "timetable/timetable_list.html", context)


@login_required(login_url="login")
@user_group('caregiver')
def timetable_delete_view(request, id):
    obj = get_object_or_404(Timetable, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "timetable/timetable_delete.html", context)

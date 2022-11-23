from django.shortcuts import render, get_object_or_404, redirect
from .forms import TimetableForm
from shelter.models import Timetable
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required


@login_required(login_url="login")
@permission_required("auth.add_user", login_url="/login", raise_exception=True)
def timetable_create_view(request):
    my_group = Group.objects.get(name="timetable")
    form = TimetableForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        my_group.user_set.add(user)
        form = TimetableForm()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "timetable/timetable_create.html", context)


@login_required(login_url="login")
@permission_required("auth.change_user", login_url="/login", raise_exception=True)
def timetable_update_view(request, id=id):
    obj = get_object_or_404(User, id=id)
    form = TimetableForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "timetable/timetable_create.html", context)


@login_required(login_url="login")
def timetable_list_view(request):   
    if request.POST.get('animalid', False):
        animalid = request.POST['animalid']
    queryset = Timetable.objects.filter(animalid=animalid)# list of objects
    queryset = queryset.order_by('time_from')
    queryset1 = queryset.filter(day='Pondelok')
    queryset2 = queryset.filter(day='Utorok')
    queryset3 = queryset.filter(day='Streda')
    queryset4 = queryset.filter(day='Stvrtok')
    queryset5 = queryset.filter(day='Piatok')
    context = {
        "object_list1": queryset1,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5
    }
    return render(request, "timetable/timetable_list.html", context)


@login_required(login_url="login")
@permission_required("auth.view_user", login_url="/login", raise_exception=True)
def timetable_detail_view(request, id):
    obj = get_object_or_404(User, id=id)
    context = {
        "object": obj
    }
    return render(request, "timetable/timetable_detail.html", context)

@login_required(login_url="login")
@permission_required("auth.delete_user", login_url="/login", raise_exception=True)
def timetable_delete_view(request, id):
    obj = get_object_or_404(User, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "timetable/timetable_delete.html", context)

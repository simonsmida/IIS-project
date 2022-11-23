from django.shortcuts import render, get_object_or_404, redirect
from .forms import TimetableForm
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
    return render(request, "timetable_edit/timetable_create.html", context)


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
    return render(request, "timetable_edit/timetable_create.html", context)


@login_required(login_url="login")
@permission_required("auth.view_user", login_url="/login", raise_exception=True)
def timetable_list_view(request):
    queryset = User.objects.filter(groups__name='timetable') # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "timetable_edit/timetable_list.html", context)


@login_required(login_url="login")
@permission_required("auth.view_user", login_url="/login", raise_exception=True)
def timetable_detail_view(request, id):
    obj = get_object_or_404(User, id=id)
    context = {
        "object": obj
    }
    return render(request, "timetable_edit/timetable_detail.html", context)

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
    return render(request, "timetable_edit/timetable_delete.html", context)

from django.shortcuts import render, get_object_or_404, redirect
from .forms import CaregiverForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required


@login_required(login_url="login")
@permission_required("auth.add_user", login_url="/login", raise_exception=True)
def caregiver_create_view(request):
    my_group = Group.objects.get(name="caregiver")
    form = CaregiverForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        my_group.user_set.add(user)
        # TODO: save?
        form = CaregiverForm()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "caregiver_edit/caregiver_create.html", context)


@login_required(login_url="login")
@permission_required("auth.change_user", login_url="/login", raise_exception=True)
def caregiver_update_view(request, id=id):
    obj = get_object_or_404(User, id=id)
    form = CaregiverForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "caregiver_edit/caregiver_create.html", context)


@login_required(login_url="login")
@permission_required("auth.view_user", login_url="/login", raise_exception=True)
def caregiver_list_view(request):
    queryset = User.objects.filter(groups__name='caregiver') # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "caregiver_edit/caregiver_list.html", context)


@login_required(login_url="login")
@permission_required("auth.view_user", login_url="/login", raise_exception=True)
def caregiver_detail_view(request, id):
    obj = get_object_or_404(User, id=id)
    context = {
        "object": obj
    }
    return render(request, "caregiver_edit/caregiver_detail.html", context)

@login_required(login_url="login")
@permission_required("auth.delete_user", login_url="/login", raise_exception=True)
def caregiver_delete_view(request, id):
    obj = get_object_or_404(User, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "caregiver_edit/caregiver_delete.html", context)

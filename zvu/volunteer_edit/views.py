from django.shortcuts import render, get_object_or_404, redirect
from .forms import VolunteerCreateForm, VolunteerChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test


@login_required(login_url="login")
@permission_required("auth.add_user", login_url="/login", raise_exception=True)
def volunteer_create_view(request):
    my_group1 = Group.objects.get(name="volunteer")
    my_group2 = Group.objects.get(name="volunteer_notrust")
    form = VolunteerCreateForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        if(form.cleaned_data['trust'] == '1'):
            my_group1.user_set.add(user)
        else:
            my_group2.user_set.add(user)
        # user.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "volunteer_edit/volunteer_create.html", context)


@login_required(login_url="login")
# @permission_required("auth.change_user", login_url="/login", raise_exception=True)
def volunteer_update_view(request, id=id):
    obj = get_object_or_404(User, id=id)
    my_group1 = Group.objects.get(name="volunteer")
    my_group2 = Group.objects.get(name="volunteer_notrust")
    form = VolunteerChangeForm(request.POST or None, instance=obj)
    if form.is_valid():
        user = form.save()
        if(form.cleaned_data['trust'] == '1'):
            my_group1.user_set.add(user)
            my_group2.user_set.remove(user)
        else:
            my_group2.user_set.add(user)
            my_group1.user_set.remove(user)
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "volunteer_edit/volunteer_create.html", context)


@login_required(login_url="login")
# @permission_required("auth.view_user", login_url="/login", raise_exception=True)
def volunteer_list_view(request):
    queryset1 = User.objects.filter(groups__name='volunteer')# list of objects
    queryset2 = User.objects.filter(groups__name='volunteer_notrust')# list of objects
    context = {
        "object_list1": queryset1,
        "object_list2": queryset2
    }
    return render(request, "volunteer_edit/volunteer_list.html", context)


@login_required(login_url="login")
# @permission_required("auth.view_user", login_url="/login", raise_exception=True)
def volunteer_detail_view(request, id):
    obj = get_object_or_404(User, id=id)
    trust = "not approved"
    if obj.groups.filter(name='volunteer').exists():
        trust = "approved"
    context = {
        "object": obj,
        "trust": trust
    }
    return render(request, "volunteer_edit/volunteer_detail.html", context)


@login_required(login_url="login")
@permission_required("auth.delete_user", login_url="/login", raise_exception=True)
def volunteer_delete_view(request, id):
    obj = get_object_or_404(User, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "volunteer_edit/volunteer_delete.html", context)

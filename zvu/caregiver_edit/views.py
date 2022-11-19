from django.shortcuts import render, get_object_or_404, redirect
from .forms import CaregiverForm
from shelter.models import Caregiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required

@permission_required("caregiver_edit.add_user", login_url="/login", raise_exception=True)
def caregiver_create_view(request):
    my_group = Group.objects.get(name="caregiver")
    form = CaregiverForm(request.POST or None)
    # user = request.POST.get("user") 
    if form.is_valid():
        user = form.save()
        my_group.user_set.add(user)
        form = CaregiverForm()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "caregiver_edit/caregiver_create.html", context)


def caregiver_update_view(request, id=id):
    obj = get_object_or_404(User, id_pecovatel=id)
    form = CaregiverForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "caregiver_edit/caregiver_create.html", context)


def caregiver_list_view(request):
    queryset = User.objects.filter(groups__name='caregiver') # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "caregiver_edit/caregiver_list.html", context)


def caregiver_detail_view(request, id):
    obj = get_object_or_404(User, id=id)
    context = {
        "object": obj
    }
    return render(request, "caregiver_edit/caregiver_detail.html", context)


def caregiver_delete_view(request, id):
    obj = get_object_or_404(User, id_pecovatel=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "caregiver_edit/caregiver_delete.html", context)

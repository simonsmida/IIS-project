from django.shortcuts import render, get_object_or_404, redirect
from .forms import CaregiverForm
from .models import Caregiver


def caregiver_create_view(request):
    form = CaregiverForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CaregiverForm()
    context = {
        'form': form
    }
    return render(request, "caregiver/caregiver_create.html", context)


def caregiver_update_view(request, id=id):
    obj = get_object_or_404(Caregiver, id_pecovatel=id)
    form = CaregiverForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "caregiver/caregiver_create.html", context)


def caregiver_list_view(request):
    queryset = Caregiver.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "caregiver/caregiver_list.html", context)


def caregiver_detail_view(request, id):
    obj = get_object_or_404(Caregiver, id_pecovatel=id)
    context = {
        "object": obj
    }
    return render(request, "caregiver/caregiver_detail.html", context)


def caregiver_delete_view(request, id):
    obj = get_object_or_404(Caregiver, id_pecovatel=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "caregiver/caregiver_delete.html", context)

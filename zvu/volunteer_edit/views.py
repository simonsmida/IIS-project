from django.shortcuts import render, get_object_or_404, redirect
from .forms import VolunteerForm
from shelter.models import Volunteer


def volunteer_create_view(request):
    form = VolunteerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VolunteerForm()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "volunteer_edit/volunteer_create.html", context)


def volunteer_update_view(request, id=id):
    obj = get_object_or_404(Volunteer, id_dobrovolnik=id)
    form = VolunteerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "volunteer_edit/volunteer_create.html", context)


def volunteer_list_view(request):
    queryset = Volunteer.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "volunteer_edit/volunteer_list.html", context)


def volunteer_detail_view(request, id):
    obj = get_object_or_404(Volunteer, id_dobrovolnik=id)
    context = {
        "object": obj
    }
    return render(request, "volunteer_edit/volunteer_detail.html", context)


def volunteer_delete_view(request, id):
    obj = get_object_or_404(Volunteer, id_dobrovolnik=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "volunteer_edit/volunteer_delete.html", context)

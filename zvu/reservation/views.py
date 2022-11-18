from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReservationForm
from shelter.models import Reservation


def reservation_create_view(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ReservationForm()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "reservation/reservation_create.html", context)


def reservation_update_view(request, id=id):
    obj = get_object_or_404(Reservation, id_rezervacie=id)
    form = ReservationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "reservation/reservation_create.html", context)


def reservation_list_view(request):
    queryset = Reservation.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "reservation/reservation_list.html", context)


def reservation_detail_view(request, id):
    obj = get_object_or_404(Reservation, id_rezervacie=id)
    context = {
        "object": obj
    }
    return render(request, "reservation/reservation_detail.html", context)


def reservation_delete_view(request, id):
    obj = get_object_or_404(Reservation, id_rezervacie=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "reservation/reservation_delete.html", context)

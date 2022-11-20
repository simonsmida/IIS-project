from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnimalForm
from shelter.models import Animal
from django.contrib.auth.decorators import login_required, permission_required
from reservation.views import reservation_create_view

@permission_required("shelter.add_animal", login_url="/login", raise_exception=True)
def animal_create_view(request):
    form = AnimalForm(request.POST or None)     
    if form.is_valid():
        form.save()
        form = AnimalForm()
        return redirect('../')
    context = {
        'form': form    
    }
    return render(request, "animals/animal_create.html", context)

@permission_required("shelter.change_animal", login_url="/login", raise_exception=True)
def animal_update_view(request, id=id):
    obj = get_object_or_404(Animal, id_zviera=id)
    form = AnimalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "animals/animal_create.html", context)


def animal_list_view(request):
    queryset = Animal.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "animals/animal_list.html", context)


def animal_detail_view(request, id):
    obj = get_object_or_404(Animal, id_zviera=id)
    context = {
        "object": obj
    }
    return render(request, "animals/animal_detail.html", context)


@permission_required("shelter.delete_animal", login_url="/login", raise_exception=True)
def animal_delete_view(request, id):
    obj = get_object_or_404(Animal, id_zviera=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "animals/animal_delete.html", context)

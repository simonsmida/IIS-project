from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnimalForm
from shelter.models import Animal
from django.contrib.auth.decorators import login_required, permission_required
from reservation.views import reservation_create_view
from django.core.paginator import Paginator


@login_required(login_url="login")
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


@login_required(login_url="login")
@permission_required("shelter.change_animal", login_url="/login", raise_exception=True)
def animal_update_view(request, id=id):
    obj = get_object_or_404(Animal, id=id)
    form = AnimalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "animals/animal_create.html", context)

def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )
    

def animal_list_view(request):
    animal_list = Animal.objects.all() # list of objects
    print(pretty_request(request))
    # pagination
    p = Paginator(animal_list, 5)
    page = request.GET.get('page')
    animals = p.get_page(page)
    context = {
        'animals': animals
    }
    return render(request, "animals/animal_list.html", context)


def animal_detail_view(request, id):
    obj = get_object_or_404(Animal, id=id)
    context = {
        "object": obj
    }
    return render(request, "animals/animal_detail.html", context)


@login_required(login_url="login")
@permission_required("shelter.delete_animal", login_url="/login", raise_exception=True)
def animal_delete_view(request, id):
    obj = get_object_or_404(Animal, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "animals/animal_delete.html", context)

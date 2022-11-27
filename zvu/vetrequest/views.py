from django.shortcuts import render, get_object_or_404, redirect
from .forms import VetrequestForm, VetrequestExamForm, VetrequestNewForm
from shelter.models import Vetrequest, Animal
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponseForbidden   
from animals.templatetags.animals_extras import has_group
from reservation.decorators import my_login_required

@my_login_required
@permission_required("shelter.add_vetrequest", login_url="login", raise_exception=True)
def vetrequest_create_view(request):
    form = VetrequestForm(request.POST or None) 
    if form.is_valid():
        vetrequest = form.save(commit=False)
        vetrequest.caregiverid = request.user
        vetrequest.save()
        return redirect('../')
    
    context = {
        'form': form
    }
    return render(request, "vetrequest/vetrequest_create.html", context)

@my_login_required
@permission_required("shelter.add_vetrequest", login_url="login", raise_exception=True)
def vetrequest_newcreate_view(request):
    form = VetrequestNewForm(request.POST or None)
            
    if form.is_valid():
        vetrequest = form.save(commit=False)
        vetrequest.caregiverid = request.user
        vetrequest.save()
        return redirect('.')
    
    context = {
        'form': form
    }
    return render(request, "vetrequest/vetrequest_newcreate.html", context)


@login_required(login_url="login")
@permission_required("shelter.change_vetrequest", login_url="login", raise_exception=True)
def vetrequest_update_view(request, id=id):
    user = request.user
    obj = get_object_or_404(Vetrequest, id=id)

    if obj.vetid == user or obj.caregiverid == user or user.is_superuser:
        form = VetrequestForm(request.POST or None, instance=obj)
         
        if form.is_valid():
            form.save()
            return redirect('../')
        
        context = {
            'form': form,
            'animalname': obj.animalid.name
        }
        return render(request, "vetrequest/vetrequest_create.html", context)
    return HttpResponseForbidden()
    

@login_required(login_url="login")
@permission_required("shelter.view_vetrequest", login_url="login", raise_exception=True)
def vetrequest_list_view(request):
    if has_group(request.user, 'vet'):
        queryset = Vetrequest.objects.filter(vetid=request.user) # list of objects
    elif has_group(request.user, 'caregiver'):
        queryset = Vetrequest.objects.filter(caregiverid=request.user) # list of objects
        
    elif request.user.is_superuser:
        queryset = Vetrequest.objects.all() # list of objects
    
    queryset = queryset.order_by('creation_date')
    queryset1 = queryset.filter(state='pending')
    queryset2 = queryset.filter(state='exam')
    queryset2 = queryset2.order_by('exam_time')
    
    # queryset2 = []
    # if request.user.is_superuser or has_group(request.user, 'caregiver'):
    #     queryset1 = Vetrequest.objects.filter(state='pending') # list of objects
    #     queryset2 = Vetrequest.objects.filter(state='finished')
    
    context = {
        "object_list1": queryset1,
        "object_list2": queryset2   
    }
    return render(request, "vetrequest/vetrequest_list.html", context)


@login_required(login_url="login")
@permission_required("shelter.view_vetrequest", login_url="login", raise_exception=True)
def vetrequest_detail_view(request, id):
    obj = get_object_or_404(Vetrequest, id=id)
    exam_form = []
    
    if request.POST.get('state', False):
        obj.state = 'exam'  
        obj.save()
        return redirect(".")
    if obj.vetid == request.user and obj.state == "exam":
        exam_form = VetrequestExamForm(request.POST or None, instance=obj)
        
        if exam_form.is_valid():
            # exam = exam_form.save(commit=False)
            obj.exam_time = exam_form.cleaned_data['exam_time']
            obj.exam_procedure = exam_form.cleaned_data['exam_procedure']
            obj.exam_protocol = exam_form.cleaned_data['exam_protocol']
            obj.state = "exam"
            obj.save()
            return redirect('../')
        
    if obj.vetid == request.user or obj.caregiverid == request.user or request.user.is_superuser:
        context = {
            "object": obj,
            "exam": exam_form
        }
        return render(request, "vetrequest/vetrequest_detail.html", context)
    return HttpResponseForbidden()

# @login_required(login_url="login")
# @permission_required("shelter.view_vetrequest", login_url="login", raise_exception=True)
# def vetrequest_finisheddetail_view(request, id):
#     obj = get_object_or_404(Vetrequest, id=id)
#     if obj.vetid == request.user or obj.caregiverid == request.user or request.user.is_superuser:
#         context = {
#             "object": obj
#         }
#         return render(request, "vetrequest/vetrequest_detail.html", context)
#     return HttpResponseForbidden()


@login_required(login_url="login")
@permission_required("shelter.delete_vetrequest", login_url="login", raise_exception=True)
def vetrequest_delete_view(request, id):
    obj = get_object_or_404(Vetrequest, id=id)
    if obj.vetid == request.user or obj.caregiverid == request.user or request.user.is_superuser:
        if request.method == "POST":
            obj.delete()
            if obj.vetid == request.user:
                return redirect('../../')
            return redirect('../')
        context = {
            "object": obj
        }
        if obj.vetid == request.user:
            return render(request, "vetrequest/vetrequest_examdelete.html", context)
        return render(request, "vetrequest/vetrequest_delete.html", context)
    return HttpResponseForbidden()
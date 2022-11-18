from django.shortcuts import render, get_object_or_404, redirect

def myadmin_view(request):
    # queryset = Caregiver.objects.all() # list of objects
    # context = {
    #     "object_list": queryset
    # }
    return render(request, "myadmin/myadmin.html", {})

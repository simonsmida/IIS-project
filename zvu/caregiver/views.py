from django.shortcuts import render

# Create your views here.
def caregiver_view(request):
    # queryset = Caregiver.objects.all() # list of objects
    # context = {
    #     "object_list": queryset
    # }
    return render(request, "caregiver/caregiver.html", {})

from django.shortcuts import render

# Create your views here.
def volunteer_view(request):
    # queryset = volunteer.objects.all() # list of objects
    # context = {
    #     "object_list": queryset
    # }
    return render(request, "volunteer/volunteer.html", {})

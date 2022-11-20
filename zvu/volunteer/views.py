from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

# Create your views here.

@login_required(login_url="login")
def volunteer_view(request):
    # queryset = volunteer.objects.all() # list of objects
    # context = {
    #     "object_list": queryset
    # }
    return render(request, "volunteer/volunteer.html", {})

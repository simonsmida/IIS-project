from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

# Create your views here.
@login_required
@user_passes_test(lambda u: u.groups.filter(name='caregiver').exists(),login_url="login")
def caregiver_view(request):
    # queryset = Caregiver.objects.all() # list of objects
    # context = {
    #     "object_list": queryset
    # }
    return render(request, "caregiver/caregiver.html", {})

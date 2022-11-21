from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponseForbidden
# Create your views here.

@login_required(login_url="login")
def volunteer_view(request):
    user = request.user
    if user.groups.filter(name='caregiver').exists() or user.is_superuser:
        return render(request, "volunteer/volunteer.html", {})
    return HttpResponseForbidden()

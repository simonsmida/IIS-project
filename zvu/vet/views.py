from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from caregiver.decorators import user_group
from shelter.models import Vetrequest

# Create your views here.
@login_required(login_url="login")
# @user_passes_test(lambda u: u.groups.filter(name='vet').exists(), login_url='../shelter/forbidden.html')
# @permission_required(perm='shelter.view_animal', raise_exception=True)
def vet_view(request):
    user = request.user
    if user.groups.filter(name='vet').exists() or user.is_superuser:
        # exists
        return render(request, "vet/vet.html", {})
    # raise PermissionDenied
    return HttpResponseForbidden()

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

# Create your views here.
@login_required(login_url="login")
#@user_passes_test(lambda u: u.groups.filter(name='caregiver').exists(), login_url='../shelter/forbidden.html')
# @permission_required(perm='shelter.view_animal', raise_exception=True)
def caregiver_view(request):
    user = request.user
    if user.groups.filter(name='caregiver').exists():
        #exists
        return render(request, "caregiver/caregiver.html", {})
    # raise PermissionDenied
    return HttpResponseForbidden()
    

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required


@login_required(login_url="login")
@permission_required("auth.view_user", login_url="/login", raise_exception=True)
def myadmin_view(request):
    # queryset = Caregiver.objects.all() # list of objects
    # context = {
    #     "object_list": queryset
    # }
    return render(request, "myadmin/myadmin.html", {})

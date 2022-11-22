import functools
from django.shortcuts import redirect

def my_login_required(view_func):

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request,*args, **kwargs)
        return redirect("/login/?next=/animals/")
    return wrapper  
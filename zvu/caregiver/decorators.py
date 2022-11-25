from django.http import HttpResponseForbidden

def user_group(*groups):
    """
    Decorator for checking given user groups as input.
    Decorator runs a function only if user has one of the specified 
    user groups. User groups are passed as a decorator parameter
    """
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.user != None:
                user = request.user
                has_valid_group = False
                for arg in groups:
                    if user.groups.filter(name=arg).exists():
                        has_valid_group = True
                if has_valid_group:
                    value = func(request, *args, **kwargs)
                    return value
                else:
                    return HttpResponseForbidden()
            else:
                return HttpResponseForbidden()
        return wrapper
    return decorator
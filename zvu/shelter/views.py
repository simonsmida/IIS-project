from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ChangePasswordForm, ChangeAccForm

from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/login.html', {})
    else:
        form = LoginForm()
    
    context = {
        'form': form
    }

    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def sign_up_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if password != confirm_password:
                return render(request, 'registration/sign_up.html', {'error': 'Passwords do not match'})

            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'registration/sign_up.html', context)


def edit_profile_view(request):
    obj = get_object_or_404(User, id=request.user.id)
    form = ChangeAccForm(request.POST or None, instance=obj)
    print("qauck")
    if form.is_valid():
        print("haf")
        form.save()
        return redirect("profile")
    else:
        print(form.errors.as_data())
    context = {
        'form': form
    }
    return render(request, "accounts/edit_profile.html", context)


def password_change_view(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if new_password != confirm_password:
                return render(request, 'accounts/change_password.html', {'error': 'Passwords do not match'})

            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return redirect('home')
            else:
                return render(request, 'accounts/change_password.html', {'error': 'Old password is not correct'})
    else:
        form = ChangePasswordForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/change_password.html', context)


def profile_view(request):
    user = get_object_or_404(User, id=request.user.id)
    context = {
        'user': user
    }
    return render(request, "accounts/profile.html", context)


def home(request):
    return render(request, 'shelter/home.html', {})

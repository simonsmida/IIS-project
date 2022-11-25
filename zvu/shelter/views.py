from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, ChangeAccForm

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

def changeacc_view(request):
    obj = get_object_or_404(User, id=request.user.id)
    form = ChangeAccForm(request.POST or None, instance=obj)
    print("qauck")
    if form.is_valid():
        print("haf")
        form.save()
        return redirect('../')
    else:
        print(form.errors.as_data())
    context = {
        'form': form
    }
    return render(request, "shelter/changeacc.html", context)


def home(request):
    return render(request, 'shelter/home.html', {})

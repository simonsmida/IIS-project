from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('sign-up', views.sign_up_view, name='sign-up'),
    path('password-change', views.password_change_view, name='password-change'),
    path('changeacc', views.changeacc_view, name='changeacc'),
    path('profile', views.profile_view, name='profile'),
]

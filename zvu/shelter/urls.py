from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('sign-up', views.sign_up_view, name='sign-up'),
    path('change-password', views.password_change_view, name='change-password'),
    path('edit-profile', views.edit_profile_view, name='edit-profile'),
    path('profile', views.profile_view, name='profile'),
    ]

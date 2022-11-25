from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('sign-up', views.sign_up_view, name='sign-up'),
    path('changeacc', views.changeacc_view, name='changeacc')
]
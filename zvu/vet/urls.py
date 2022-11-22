from django.urls import path

from .views import vet_view

app_name = 'vet'
urlpatterns = [
    path('', vet_view, name='vet'),
]
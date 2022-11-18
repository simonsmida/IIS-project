from django.urls import path

from .views import myadmin_view

app_name = 'myadmin'
urlpatterns = [
    path('', myadmin_view, name='myadmin'),
]
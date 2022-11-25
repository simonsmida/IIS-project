from django.urls import path

from .views import volunteer_view

app_name = 'volunteer'
urlpatterns = [
    path('', volunteer_view, name='volunteer')
]
from django.urls import path
from .views import (
    animal_create_view, 
    animal_detail_view, 
    animal_delete_view,
    animal_list_view,
    animal_update_view,   
)

app_name = 'animals'
urlpatterns = [
    path('', animal_list_view, name='animal-list'),
    path('create/', animal_create_view, name='animal-create'),
    path('<int:id>/', animal_detail_view, name='animal-detail'),
    path('<int:id>/update/', animal_update_view, name='animal-update'),
    path('<int:id>/delete/', animal_delete_view, name='animal-delete'),
]
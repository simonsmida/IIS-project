from django.urls import path
from .views import (
    caregiver_create_view, 
    caregiver_detail_view, 
    caregiver_delete_view,
    caregiver_list_view,
    caregiver_update_view,
)

from animals.views import (
    animal_list_view
)

app_name = 'caregiver_edit'
urlpatterns = [
    path('', caregiver_list_view, name='caregiver-list'),
    path('create/', caregiver_create_view, name='caregiver-create'),
    path('<int:id>/', caregiver_detail_view, name='caregiver-detail'),
    path('<int:id>/update/', caregiver_update_view, name='caregiver-update'),
    path('<int:id>/delete/', caregiver_delete_view, name='caregiver-delete'),
    # path('animals/', animal_list_view, name='animal-list'),
]
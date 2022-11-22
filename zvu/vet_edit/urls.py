from django.urls import path
from .views import (
    vet_create_view, 
    vet_detail_view, 
    vet_delete_view,
    vet_list_view,
    vet_update_view,
)


app_name = 'vet_edit'
urlpatterns = [
    path('', vet_list_view, name='vet-list'),
    path('create/', vet_create_view, name='vet-create'),
    path('<int:id>/', vet_detail_view, name='vet-detail'),
    path('<int:id>/update/', vet_update_view, name='vet-update'),
    path('<int:id>/delete/', vet_delete_view, name='vet-delete'),
    # path('animals/', animal_list_view, name='animal-list'),
]
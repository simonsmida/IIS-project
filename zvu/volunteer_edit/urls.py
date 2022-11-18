from django.urls import path
from .views import (
    volunteer_create_view, 
    volunteer_detail_view, 
    volunteer_delete_view,
    volunteer_list_view,
    volunteer_update_view,
)

app_name = 'volunteer_edit'
urlpatterns = [
    path('', volunteer_list_view, name='volunteer-list'),
    path('create/', volunteer_create_view, name='volunteer-create'),
    path('<int:id>/', volunteer_detail_view, name='volunteer-detail'),
    path('<int:id>/update/', volunteer_update_view, name='volunteer-update'),
    path('<int:id>/delete/', volunteer_delete_view, name='volunteer-delete'),
    # path('animals/', animal_list_view, name='animal-list'),
]
from django.urls import path

from .views import myadmin_view

app_name = 'myadmin'
urlpatterns = [
    path('', myadmin_view, name='myadmin'),
    # path('create/', caregiver_create_view, name='caregiver-list'),
    # path('<int:id>/', caregiver_detail_view, name='caregiver-detail'),
    # path('<int:id>/update/', caregiver_update_view, name='caregiver-update'),
    # path('<int:id>/delete/', caregiver_delete_view, name='caregiver-delete'),
    # path('animals/', animal_list_view, name='animal-list'),
]
from django.urls import path
from .views import (
    reservation_create_view, 
    reservation_detail_view, 
    reservation_delete_view,
    reservation_list_view,
    reservation_update_view,
    reservation_sent_view,
    reservation_walklist_view
)

from animals.views import (
    animal_list_view
)

app_name = 'reservation'
urlpatterns = [
    path('', reservation_list_view, name='reservation-list'),
    path('walks/', reservation_walklist_view, name='reservation-walklist'),
    path('create/', reservation_create_view, name='reservation-create'),
    path('<int:id>/', reservation_detail_view, name='reservation-detail'),
    path('<int:id>/update/', reservation_update_view, name='reservation-update'),
    path('<int:id>/delete/', reservation_delete_view, name='reservation-delete'),
    path('sent/', reservation_sent_view, name='reservation-sent')
    # path('animals/', animal_list_view, name='animal-list'),
] 

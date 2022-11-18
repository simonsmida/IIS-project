from django.urls import path

from .views import volunteer_view

app_name = 'volunteer'
urlpatterns = [
    path('', volunteer_view, name='volunteer'),
    # path('create/', volunteer_create_view, name='volunteer-list'),
    # path('<int:id>/', volunteer_detail_view, name='volunteer-detail'),
    # path('<int:id>/update/', volunteer_update_view, name='volunteer-update'),
    # path('<int:id>/delete/', volunteer_delete_view, name='volunteer-delete'),
    # path('animals/', animal_list_view, name='animal-list'),
]
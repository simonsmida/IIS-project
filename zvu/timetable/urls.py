from django.urls import path
from .views import (
    timetable_create_view, 
    timetable_detail_view, 
    timetable_delete_view,
    timetable_list_view,
    timetable_update_view,
)


app_name = 'timetable'
urlpatterns = [
    path('', timetable_list_view, name='timetable-list'),
    path('create/', timetable_create_view, name='timetable-create'),
    path('<int:id>/', timetable_detail_view, name='timetable-detail'),
    path('<int:id>/update/', timetable_update_view, name='timetable-update'),
    path('<int:id>/delete/', timetable_delete_view, name='timetable-delete'),
]
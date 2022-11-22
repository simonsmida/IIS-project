from django.urls import path
from .views import (
    vetrequest_create_view, 
    vetrequest_detail_view, 
    vetrequest_delete_view,
    vetrequest_list_view,
    vetrequest_update_view,
)

app_name = 'vetrequest'
urlpatterns = [
    path('', vetrequest_list_view, name='vetrequest-list'),
    path('create/', vetrequest_create_view, name='vetrequest-create'),
    path('<int:id>/', vetrequest_detail_view, name='vetrequest-detail'),
    path('<int:id>/update/', vetrequest_update_view, name='vetrequest-update'),
    path('<int:id>/delete/', vetrequest_delete_view, name='vetrequest-delete'),
    # path('animals/', animal_list_view, name='animal-list'),
] 
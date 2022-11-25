from django.urls import path

from .views import (
    caregiver_view,
    manage_volunteers_view,
    edit_animals_view,
    create_schedules_view,
    register_walks_view,
    create_vet_request_view,
    verify_volunteers_view,
    unverify_volunteers_view,
    approve_res_view,
    get_reservations,
    approve_reservation,
    save_walk_time,

)

from animals.views import (
    animal_create_view,
    animal_detail_view,
    animal_delete_view,
    animal_list_view,
    animal_update_view   
)

app_name = 'caregiver'
urlpatterns = [
    path('', manage_volunteers_view, name='caregiver'),
    path('manage_volunteers/', manage_volunteers_view, name='manage-volunteers'),
    path('manage_volunteers/verify', verify_volunteers_view, name='verify-volunteers'),
    path('manage_volunteers/unverify', unverify_volunteers_view, name='unverify-volunteers'),
    path('edit_animals/', edit_animals_view, name='edit-animals'),
    path('edit_animals/<int:id>/update', animal_update_view, name='update-animal'),
    path('edit_animals/<int:id>/delete', animal_delete_view, name='delete-animal'),
    path('edit_animals/create', animal_create_view, name='create-animal'),
    path('create_schedules/', create_schedules_view, name='create-schedules'),

    path('approve_res/', approve_res_view, name='approve-res'),
    path('approve_res/get_reservations', get_reservations, name='approve-res-list'),
    path('approve_res/approve', approve_reservation, name='approve-res'),
    

    path('register_walks/', register_walks_view, name='register-walks'),
    path('register_walks/save/', save_walk_time, name='saev-walk-time'),

    path('create_vet_request/', create_vet_request_view, name='create-vet-request'),
    
    # path('create/', caregiver_create_view, name='caregiver-list'),
    # path('<int:id>/', caregiver_detail_view, name='caregiver-detail'),
    # path('<int:id>/update/', caregiver_update_view, name='caregiver-update'),
    # path('<int:id>/delete/', caregiver_delete_view, name='caregiver-delete'),
    # path('animals/', animal_list_view, name='animal-list'),
]
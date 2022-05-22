from django.urls import path
from pets.views import pet_list, add_pet, pet_alert, pet_alert_blank

urlpatterns = [
    path('', pet_list, name="pet_list"),
    path('add_pet/', add_pet, name='add_pet'),
    path('pet_alert/', pet_alert, name='pet_alert'),
    path('pet_alert_blank/', pet_alert_blank, name='pet_alert_blank'),
]

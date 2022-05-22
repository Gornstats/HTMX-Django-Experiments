from django.urls import path
from pets.views import pet_list, add_pet, pet_alert

urlpatterns = [
    path('', pet_list, name="pet_list"),
    path('add_pet/', add_pet, name='add_pet'),
    path('pet_alert/', pet_alert, name='pet_alert'),
]

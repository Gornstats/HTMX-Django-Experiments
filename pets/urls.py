from django.urls import path
from pets.views import pet_list

urlpatterns = [
    path('', pet_list, name="pet_list"),
]

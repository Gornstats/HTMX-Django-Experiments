from django.urls import path
from keyboard.views import button_press, change_colour

urlpatterns = [
    path('', button_press, name="button_press"),
    path("change/<str:colour>/", change_colour, name="change_colour"),
]

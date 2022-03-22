from django.urls import path
from keyboard.views import button_press

urlpatterns = [
    path('', button_press, name="button_press"),
]

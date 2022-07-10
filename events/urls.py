from django.urls import path
from events.views import index, check_spaces

urlpatterns = [
    path('', index, name='index'),
    path('check_spaces/', check_spaces, name='check_spaces'),
]

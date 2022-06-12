from django.urls import path
from modals.views import index

urlpatterns = [
    path('', index, name="index"),
]

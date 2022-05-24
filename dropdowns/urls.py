from django.urls import path
from dropdowns.views import index

urlpatterns = [
    path('', index, name="index"),
]

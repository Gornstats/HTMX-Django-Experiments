from django.urls import path
from dropdowns.views import index, options

urlpatterns = [
    path('', index, name="index"),
    path('options', options, name="options"),
]

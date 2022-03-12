from django.urls import path
from crud.views import live_edit

urlpatterns = [
    path('', live_edit, name="live_edit"),
]
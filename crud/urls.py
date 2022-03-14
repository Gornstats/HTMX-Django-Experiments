from django.urls import path
from crud.views import live_edit, edit_person, get_person, update_person

urlpatterns = [
    path('', live_edit, name="live_edit"),
    path("edit/<int:pk>/", edit_person, name="edit_person"),
    path("person/<int:pk>/", get_person, name="get_person"),
    path("update/<int:pk>/", update_person, name="update_person"),
]
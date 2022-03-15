from django.urls import path
from crud.views import (live_edit, edit_person, get_person, update_person, 
                        create_person, create, cancel_create, delete_person)

urlpatterns = [
    path('', live_edit, name="live_edit"),
    path("edit/<int:pk>/", edit_person, name="edit_person"),
    path("person/<int:pk>/", get_person, name="get_person"),
    path("update/<int:pk>/", update_person, name="update_person"),
    path("create_person/", create_person, name="create_person"),
    path("create/", create, name="create"),
    path("cancel_create/", cancel_create, name="cancel_create"),
    path("delete/<int:pk>/", delete_person, name="delete_person"),
]
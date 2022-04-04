from django.urls import path
from certificate.views import certificate_builder, edit_name, edit_qual, edit_date, edit_sign, generate_pdf

urlpatterns = [
    path('', certificate_builder, name="certificate_builder"),
    path('name/', edit_name, name="edit_name"),
    path('qual/', edit_qual, name="edit_qual"),
    path('date/', edit_date, name="edit_date"),
    path('sign/', edit_sign, name="edit_sign"),
    path('download/', generate_pdf, name="generate_pdf"),
]

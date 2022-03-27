from django.urls import path
from certificate.views import certificate_builder

urlpatterns = [
    path('', certificate_builder, name="certificate_builder"),
]

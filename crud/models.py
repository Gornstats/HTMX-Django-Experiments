from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField(max_length=50, blank=True)

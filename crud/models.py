from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=50)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

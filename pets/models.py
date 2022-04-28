from django.db import models

class Pet(models.Model):
    pet_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.pet_name

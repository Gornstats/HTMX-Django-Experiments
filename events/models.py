from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=120)
    number_of_places = models.IntegerField(default=3)
    
    def __str__(self):
        return self.name
    
class EventUser(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='users')

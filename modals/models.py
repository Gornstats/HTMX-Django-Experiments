from django.db import models

# Feedback model to store feedback entered through modal form
class Feedback(models.Model):
    message = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

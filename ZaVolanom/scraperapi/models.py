from django.db import models

# Create your models here.
class EventListener(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
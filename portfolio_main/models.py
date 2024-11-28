from django.db import models
from django.urls import reverse


# Create your models here.

class Works(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

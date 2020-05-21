from django.db import models
import json
# Create your models here.

class Work(models.Model):
    service = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=2000, null=True)
    budget = models.CharField(max_length=50, null=True)
    deadline = models.CharField(max_length=500, null=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.service

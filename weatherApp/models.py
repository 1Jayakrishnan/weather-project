from django.db import models

# Create your models here.
class weatherDb(models.Model):
    city = models.CharField(max_length=20, null=True, blank=True)
    temperature = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=20, null=True, blank=True)
    pressure = models.CharField(max_length=20, null=True, blank=True)
    humidity = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
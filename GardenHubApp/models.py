from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class GardenNeighbourhood(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


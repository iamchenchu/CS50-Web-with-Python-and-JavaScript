from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"



# Create your models here.
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete = models.CASCADE)       #origin = models.CharField(max_length = 64)
    destination = models.CharField(max_length = 64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"
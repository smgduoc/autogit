from django.db import models
from django.utils import timezone



class Vehi(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    marcamodelo = models.CharField(max_length=200)
    annio = models.IntegerField(blank=False, default=2000)
    kilom = models.IntegerField(blank=False, default=10)
    manual = models.BooleanField
    camion = models.BooleanField
    infoad = models.CharField(max_length=200)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.marcamodelo
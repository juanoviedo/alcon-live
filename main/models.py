from django.db import models
from datetime import datetime, date

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200, unique=True)
    creationdate = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.name

class PDay(models.Model):
    day = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    cows = models.FloatField(null=True, blank=True)
    milk = models.FloatField(null=True, blank=True)
    feed = models.FloatField(null=True, blank=True)
    cowmilk = models.FloatField(null=True, blank=True) # leche / vacas
    efficiency = models.FloatField(null=True, blank=True) # leche / concentrado
    conversion = models.FloatField(null=True, blank=True) # concentrado / leche
    status = models.CharField(max_length=30)
    obs = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.date)
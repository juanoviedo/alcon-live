from django.db import models
from datetime import datetime, date

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200, unique=True)
    creationdate = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.name

class Day(models.Model):
    day = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    totalcows = models.IntegerField(null=True, blank=True)
    animalfeed = models.IntegerField(null=True, blank=True)
    totalmilk = models.IntegerField(null=True, blank=True)
    
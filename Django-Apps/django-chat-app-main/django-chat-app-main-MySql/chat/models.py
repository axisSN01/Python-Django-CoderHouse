from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    id = models.AutoField(primary_key=True)  # Define a primary key field
    name = models.CharField(max_length=1000)


class Message(models.Model):
    id = models.AutoField(primary_key=True)  # Define a primary key field
    value = models.TextField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.TextField(max_length=1000000)
    room = models.TextField(max_length=1000000)
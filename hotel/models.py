from django.db import models

# Create your models here.
class Room(models.Model):
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.CharField(max_length=50)
from django.db import models

# Create your models here.
class BookingTable(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    booking_date = models.DateTimeField()

class MenuTable(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

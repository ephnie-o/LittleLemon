from django.db import models

# Create your models here.
class BookingTable(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    booking_date = models.DateTimeField()

    def get_item(self):
        return f'{self.name} ; Number of guests: {str(self.no_of_guest)} ; Date: {str(self.booking_date)}'

class MenuTable(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

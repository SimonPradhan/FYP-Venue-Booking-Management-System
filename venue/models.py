from django.db import models
from user.models import UserCustomer, UserVendor
# Create your models here.

class Venue(models.Model):
    username = models.ForeignKey(UserVendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price = models.IntegerField()
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "venue"

class Booking(models.Model):
    username = models.ForeignKey(UserCustomer, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=100)
    eventType = models.CharField(max_length=100)
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(max_length=500)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "booking"
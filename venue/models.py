from django.db import models

# Create your models here.

class Venue(models.Model):
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
from django.db import models

# Create your models here.
class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField()
    def __str__(self):
        return self.name
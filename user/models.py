from django.db import models

# Create your models here. 
class UserCustomer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "usercustomer"

class UserVendor(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "uservendor"
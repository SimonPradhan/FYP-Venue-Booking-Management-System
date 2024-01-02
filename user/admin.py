from django.contrib import admin
from .models import UserCustomer, UserVendor
# Register your models here.

admin.site.register(UserCustomer)
admin.site.register(UserVendor)
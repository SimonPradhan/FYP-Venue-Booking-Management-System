from django.contrib import admin
import venue.models

# Register your models here.
admin.site.register(venue.models.Venue)
admin.site.register(venue.models.Booking)
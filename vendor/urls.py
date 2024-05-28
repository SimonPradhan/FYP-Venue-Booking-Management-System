from django.urls import path
from .views import vendor, details, showBookings, addVenue

app_name = 'vendor'
urlpatterns = [
    path('vendor/',vendor, name='vendor'),
    path('details/',details, name='details'),
    path('showBookings/',showBookings, name='showBookings'),
    path('addVenue/',addVenue, name='addVenue'),
]
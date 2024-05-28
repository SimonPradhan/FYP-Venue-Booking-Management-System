from django.urls import path
from .views import vendor, details, showBookings, addVenue, showVenue, updateVenue

app_name = 'vendor'
urlpatterns = [
    path('vendor/',vendor, name='vendor'),
    path('details/',details, name='details'),
    path('showBookings/',showBookings, name='showBookings'),
    path('showVenue/',showVenue, name='showVenue'),
    path('addVenue/',addVenue, name='addVenue'),
    path('updateVenue/<int:id>',updateVenue, name='updateVenue')
]
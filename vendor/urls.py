from django.urls import path
from .views import vendor, details, showBookings

app_name = 'vendor'
urlpatterns = [
    path('vendor/',vendor, name='vendor'),
    path('details/',details, name='details'),
    path('showBookings/<int:id>',showBookings, name='showBookings')
]
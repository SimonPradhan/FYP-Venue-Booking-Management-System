from django.shortcuts import render
from venue.models import Booking, Venue
from user.models import UserVendor

# Create your views here.
def vendor(request):
    vendor = UserVendor.objects.get(username=request.user)

    return render(request,'vendor/dashboard.html', {"vendor":vendor})

def details(request):
    return render(request,'vendor/details.html', {"name":"name"})

def showBookings(request):
    vendor = UserVendor.objects.get(username=request.user)
    try:
        # Retrieve the Venue associated with the UserVendor
        venue = Venue.objects.get(username=vendor)
    except Venue.DoesNotExist:
        # Handle the case where no venue is associated with the vendor
        venue = None
    print(vendor, venue)

    print(vendor, venue)
    context = {
        'bookings': Booking.objects.filter(venue=venue),
        'vendor': vendor,
    }
    return render(request,'vendor/viewBooking.html', context)
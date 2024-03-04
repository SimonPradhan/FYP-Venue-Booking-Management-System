from django.shortcuts import render
from venue.models import Booking, Venue
from user.models import UserVendor

# Create your views here.
def vendor(request):
    vendor_id = request.session.get('vendor_id')
    print(vendor_id)
    vendor = UserVendor.objects.get(id = vendor_id)

    return render(request,'vendor/dashboard.html', {"vendor":vendor})

def details(request):
    return render(request,'vendor/details.html', {"name":"name"})

def addVenue(request):

    return render(request,'vendor/addVenue.html', {"name":"name"})

def showBookings(request):
    vendor_id = request.session.get('vendor_id')
    user = UserVendor.objects.get(id=vendor_id)
    # cust = UserCustomer.6
    # Retrieve all venues associated with the UserVendor
    venues = Venue.objects.filter(vendor_id=vendor_id)
    
    context = {
        'bookings': Booking.objects.filter(venue__in=venues).values(),
        'vendor': user,
        'venues': venues,  # Pass the venues to the template if needed
    }
    return render(request, 'vendor/viewBooking.html', context)

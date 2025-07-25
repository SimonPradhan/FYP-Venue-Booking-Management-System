from django.shortcuts import render
from venue.models import Booking, Venue
from user.models import UserVendor

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.

def vendor(request):
    vendor_id = request.session.get('vendor_id')
    vendor = UserVendor.objects.get(id = vendor_id)
    print(vendor_id)
    totalbooking = Booking.objects.filter().count()
    # totalCustomer = Booking.objects.values('username').distinct().count()
    unique_customers = set(Booking.objects.values_list('username_id', flat=True))
    totalCustomer = len(unique_customers)

    return render(request,'vendor/dashboard.html', {"vendor":vendor, "totalbooking":totalbooking, "totalCustomer":totalCustomer})

def details(request):
    return render(request,'vendor/details.html', {"name":"name"})

def addVenue(request):
    if request.method == 'POST':
        vendor_id = request.session.get('vendor_id')
        print(vendor_id)
        vendor = get_object_or_404(UserVendor, id=vendor_id)
        
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        price = request.POST.get('price')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Create a new Venue object and save it
        venue = Venue(
            vendor_id=vendor,
            venuename=name,
            address=address,
            capacity=capacity,
            price=price,
            phone=phone,
            image=image,
            description=description
        )
        venue.save()
        return render(request, 'vendor/dashboard.html', {"vendor": vendor})

    else:
        vendor_id = request.session.get('vendor_id')
        vendor = get_object_or_404(UserVendor, id=vendor_id)
        return render(request, 'vendor/addVenue.html', {"vendor": vendor})

def showBookings(request):
    vendor_id = request.session.get('vendor_id')
    user = UserVendor.objects.get(id= vendor_id)
    # cust = UserCustomeror.objects.get(id=v
    # Retrieve all venues associated with the UserVendor
    venues = Venue.objects.filter(vendor_id=vendor_id)
    print(venues, user, vendor_id)
    context = {
        'bookings': Booking.objects.filter(venue__in=venues),
        'vendor': user,
        'venues': venues,  # Pass the venues to the template if needed
    }
    print(context)
    return render(request, 'vendor/viewBooking.html', context)

def showVenue(request):
    vendor_id = request.session.get('vendor_id')
    user = UserVendor.objects.get(id=vendor_id)
    # Retrieve all venues associated with the UserVendor
    venues = Venue.objects.filter(vendor_id=vendor_id)
    print(venues, user, vendor_id)
    context = {
        'venues': venues,
        'vendor': user,
    }
    print(context)
    return render(request, 'vendor/venues.html', context)

def updateVenue(request, id):
    venue = get_object_or_404(Venue, id=id)

    if request.method == 'POST':
        venue.venuename = request.POST.get('name')
        venue.capacity = request.POST.get('capacity')
        venue.price = request.POST.get('price')
        venue.phone = request.POST.get('phone')
        venue.address = request.POST.get('address')
        venue.description = request.POST.get('description')
        if request.FILES.get('image'):
            venue.image = request.FILES.get('image')
        venue.save()
        return HttpResponseRedirect('/vendor/showVenue/')
    
    return render(request, 'vendor/updateVenue.html', {"venue": venue})
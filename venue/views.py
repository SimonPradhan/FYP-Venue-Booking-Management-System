from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Venue, Booking, UserCustomer
from django.core.serializers.json import DjangoJSONEncoder 
import json

from django.shortcuts import render
from .models import Venue

def home(request):
    list_venue = Venue.objects.all()
    name = request.GET.get('name')
    location = request.GET.get('location')
    
    if name:
        list_venue = list_venue.filter(venuename__icontains=name)
    if location:
        list_venue = list_venue.filter(address__icontains=location)
    
    return render(request, 'events/home.html', {'list_venue': list_venue, 'name': name, 'location': location})



def gallery(request):
    return render(request,'events/gallery.html')

def contactus(request):
    return render(request,'events/contactus.html')

def payment(request):
    url = "https://khalti.com/api/v2/merchant-transaction/<idx>/"
    headers = {
        "Authorization": "Key test_secret_key_f59e8b7d18b4499ca40f68195a846e9b"
        }

    response = request.get(url, headers = headers)
    return render(request,'events/khaltipayment.html')

def explore(request):
    list_venue = Venue.objects.all()
    return render(request,'events/explore.html', {"list_venue":list_venue})

def partData(request, id):
    venue = Venue.objects.get(id=id)
    request.session['venue_id'] = id
    bookingdata=Booking.objects.filter(venue_id=id).values()
    booking_list = list(bookingdata)
    print(booking_list)
    for booking in booking_list:
        booking['date'] = booking['date'].strftime('%Y-%m-%d') if booking['date'] else None
        booking['time'] = booking['time'].strftime('%H:%M') if booking['time'] else None

    context ={
        "venue": venue,
        "booking_data": json.dumps(booking_list, cls=DjangoJSONEncoder),  # Serialize to JSON
    }
    return render(request, "events/venue.html", context)
#     return render(request,'events/message.html'


@csrf_exempt
def booking(request):
    # Retrieve user_id and venue_id from session
    user_id = request.session.get('user_id')
    venue_id = request.session.get('venue_id')

    # Retrieve user and venue objects or return 404 if not found
    user = get_object_or_404(UserCustomer, id=user_id)
    venue = get_object_or_404(Venue, id=venue_id)

    if request.method == 'POST':
        eventName = request.POST.get('eventName')
        eventType = request.POST.get('eventType')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        message = request.POST.get('message')

        # Validate input data (e.g., check if date is in the future)
        # Perform any necessary validation checks here
        
        # Create booking object and save it to the database
        with transaction.atomic():
            booking = Booking.objects.create(
                username=user,
                venue=venue,
                eventName=eventName,
                eventType=eventType,
                date=date,
                time=time,
                guests=guests,
                message=message
            )

        # Render the khaltipayment.html template with appropriate context
        return render(request, 'events/khaltipayment.html', {'venue': venue, 'user': user, 'booking': booking})

    # Return HttpResponse or render a template for GET requests
    return render(request, 'events/venue.html', {'venue': venue})
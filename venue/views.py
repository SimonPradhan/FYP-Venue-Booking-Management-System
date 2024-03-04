from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Venue, Booking, UserCustomer
from django.core.serializers.json import DjangoJSONEncoder 
import json

def home(request):
    list_venue = Venue.objects.all()
    search_data = request.GET.get('search')
    if search_data != "" and search_data is not None:
        data = Venue.objects.filter(title__icontains=search_data)
        return render(request, 'events/home.html', {'data': data})
    return render(request,'events/home.html', {"name":"name", "list_venue":list_venue})

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
    user_id = request.session.get('user_id')  # Retrieve user_id from session
    venue_id = request.session.get('venue_id')  # Retrieve venue_id from session
    # try:
    user = UserCustomer.objects.get(id=user_id)
    venue = Venue.objects.get(id=venue_id)
    print(venue)
    # except UserCustomer.DoesNotExist:
    #     # Handle case where user is not found in the database
    #     return HttpResponse("User does not exist.")
    # except Venue.DoesNotExist:
    #     # Handle case where venue is not found in the database
    #     return HttpResponse("Venue does not exist.")

    if request.method == 'POST':
        eventName = request.POST.get('eventName')
        eventType = request.POST.get('eventType')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        message = request.POST.get('message')
        
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
        booking.save()
        return render(request, 'events/khaltipayment.html', {'venue': venue, 'user': user, 'booking': booking})

    return render(request, 'events/venue.html', {'venue': venue})

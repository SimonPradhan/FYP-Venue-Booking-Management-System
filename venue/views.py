from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse       
from .models import Venue, Booking, UserCustomer
from django.core.serializers.json import DjangoJSONEncoder 
import json

from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from payments.views import khalti

def home(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        profile = UserCustomer.objects.get(id=user_id)
    else:
        profile = None

    list_venue = Venue.objects.all()
    categories = ["Banquet Hall", "Hotel", "Resort", "Restaurant"]
    query = request.GET.get('query', '')  # Get the search query from the request
    if query:
        # Filter venues based on the query for both venuename and location
        list_venue = list_venue.filter(Q(venuename__icontains=query) | Q(address__icontains=query))
    
    return render(request, 'events/home.html', {'list_venue': list_venue, 'query': query, 'profile': profile, 'categories': categories})



def gallery(request):
    return render(request,'events/gallery.html')

def contactus(request):
    return render(request,'events/contactus.html')

def payment(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        profile = UserCustomer.objects.get(id=user_id)
    else: 
        profile = None

    venue_id = request.session.get('venue_id')
    user_id = request.session.get('user_id')
    venue = Venue.objects.get(id = venue_id)
    user = UserCustomer.objects.get(id = user_id)
    # url = "https://a.khalti.com/api/v2/merchant-transaction/<idx>/"
    # headers = {
    #     "Authorization": "Key test_secret_key_7f0d2106c6e94bc2b98a108cbf9d7bf6"
    #     }

    # response = request.get(url, headers = headers)
    return render(request,'events/khaltipayment.html', {'venue': venue, 'user': user, 'profile': profile})

def explore(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        profile = UserCustomer.objects.get(id=user_id)
    else:
        profile = None
    list_venue = Venue.objects.all()
    query = request.GET.get('query', '')  # Get the search query from the request
    if query:
        # Filter venues based on the query for both venuename and location
        list_venue = list_venue.filter(Q(venuename__icontains=query) | Q(address__icontains=query))
    return render(request,'events/explore.html', {"list_venue":list_venue, "query": query ,"profile":profile})

def partData(request, id):
    user_id = request.session.get('user_id')
    profile = UserCustomer.objects.get(id=user_id) if user_id else None
    venue = Venue.objects.get(id=id)
    request.session['venue_id'] = id
    bookingdata = Booking.objects.filter(venue_id=id).values()
    booking_list = list(bookingdata)
    for booking in booking_list:
            booking['date'] = booking['date'].strftime('%Y-%m-%d') if booking['date'] else None
            booking['time'] = booking['time'].strftime('%H:%M') if booking['time'] else None

    context = {
        "profile": profile,
        "venue": venue,
        "booking_data": json.dumps(booking_list, cls=DjangoJSONEncoder),
    }
    return render(request, "events/venue.html", context)

@csrf_exempt
def booking(request):
    user_id = request.session.get('user_id')
    venue_id = request.session.get('venue_id')

    # Retrieve user and venue objects or return 404 if not found
    user = get_object_or_404(UserCustomer, id=user_id)
    venue = get_object_or_404(Venue, id=venue_id)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Log the incoming data
        print('Incoming data:', data)
        
        payment_payload = data.get('payload')
        booking_data = data.get('bookingData')

        if payment_payload and booking_data:
            booking = Booking.objects.create(
                username=user,
                venue=venue,
                eventName=booking_data['eventName'],
                eventType=booking_data['eventType'],
                date=booking_data['date'],
                time=booking_data['time'],
                guests=booking_data['guests'],
                message=booking_data['message'],
                amount=booking_data['cost'],
                transaction_id=payment_payload['idx'],
                token=payment_payload['token']
            )
            booking.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failure', 'message': 'Invalid data'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request method'})
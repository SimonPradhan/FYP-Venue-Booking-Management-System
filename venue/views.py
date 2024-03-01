from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from .models import Venue, Booking, UserCustomer

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
    context ={
        "venue":venue,
    }
    return render(request, "events/venue.html", context)
#     return render(request,'events/message.html'

@csrf_exempt
def booking(request, id):

    username = request.user

    user = UserCustomer.objects.get(username=username)

    venue = Venue.objects.get(id=id)
    print(venue, user)
    if request.method == 'POST':
        #username = request.POST.get('user')
        eventName = request.POST.get('eventName')
        eventType = request.POST.get('eventType')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        message = request.POST.get('message')
        
        print(user, venue, eventName, eventType, date, time, guests, message)
        booking = Booking.objects.create(
            username= user,
            venue=venue,
            eventName=eventName,
            eventType=eventType,
            date=date,
            time=time,
            guests=guests,
            message=message
        )
        booking.save()
        return render(request,'events/khaltipayment.html', {'venue':venue, 'user':user, 'booking':booking})
    return render(request,'events/venue.html',{'venue':venue})


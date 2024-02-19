from django.shortcuts import render 
from .models import Venue

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
    return render(request,'events/khaltipayment.html')

def explore(request):
    list_venue = Venue.objects.all()
    return render(request,'events/explore.html', {"list_venue":list_venue})

def partData(request, id):
    venue = Venue.objects.get(id=id)
    context ={
        "venue":venue
    }
    return render(request, "events/venue.html", context)
#     return render(request,'events/message.html'

def booking(request):
    
    return render(request,'events/booking.html')
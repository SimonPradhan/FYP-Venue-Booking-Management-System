from django.shortcuts import render 
from .models import Venue

def home(request):
    list_venue = Venue.objects.all()
    return render(request,'events/home.html', {"name":"name", "list_venue":list_venue})

def vendor(request):
    return render(request,'events/vendor.html', {"name":"name"})


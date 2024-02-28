from django.shortcuts import render

# Create your views here.
def vendor(request):
    return render(request,'vendor/dashboard.html', {"name":"name"})

def details(request):
    return render(request,'vendor/details.html', {"name":"name"})

def showBookings(request):
    
    return render(request,'vendor/viewBooking.html', {"name":"name"})
from django.shortcuts import render

# Create your views here.
def vendor(request):
    return render(request,'vendor/dashboard.html', {"name":"name"})
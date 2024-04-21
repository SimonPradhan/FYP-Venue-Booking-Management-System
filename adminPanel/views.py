from django.shortcuts import render, redirect
from user.models import UserVendor, UserCustomer
from venue.models import Booking
from user.views import UserVendor
from django.contrib.auth.models import User
from django.contrib import messages
# def index(request):
#     return render(request, 'adminPanel/adminDashboarad.html', {"name":"name"})

def adminDashboard(request):
    totalVendor = UserVendor.objects.count()
    totalCust = UserCustomer.objects.count()
    totalbooking = Booking.objects.count()
    context = {
        'totalVendor': totalVendor,
        'totalCust': totalCust,
        'totalbooking': totalbooking
    }
    return render(request, 'adminPanel/adminDasboard.html', context)

#vendors
def add_vendor(request):
    vendor = UserVendor.objects.all()
    if request.method == 'POST':
        username=request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        confirmpassword = request.POST.get('confirmpassword')
        phone = request.POST.get('phone') 
        address = request.POST.get('address') 
        # if :
        #     messages.success(request,('Passwords match!'))
        #     return redirect('user:signup')
        
        if password != confirmpassword or UserVendor.objects.filter(email=email).exists():
            messages.success(request,('Email already exists!'))
            return redirect('user:signup')
        else:
            vendor = User.objects.create_user(username=username, email=email, password=password)
            vendor.save()

            vendorData = UserVendor.objects.create(
                username=username,
                name=name,
                email=email,
                password=password,
                phone=phone,
                address=address
            ) 
            vendorData.save()
            messages.success(request,('Vendor Added Successfully!'))
    return render(request, 'adminPanel/addVendor.html', {"vendor":vendor})

def delete_vendor(request, id):
    vendor = UserVendor.objects.get(id=id)
    vendor.delete()
    return render(request, 'adminPanel/showVendor.html', {"vendor":vendor})

def update_vendor(request, id):
    vendor = UserVendor.objects.get(id=id)
    if request.method == 'POST':
        username=request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        phone = request.POST.get('phone') 
        address = request.POST.get('address') 
        
        vendor.username = username
        vendor.name = name
        vendor.email = email
        vendor.password = password
        vendor.phone = phone
        vendor.address = address
        vendor.save()
        return render(request, 'adminPanel/showVendor.html', {"vendor":vendor})
    return render(request, 'adminPanel/updateVendor.html', {"vendor":vendor})

def show_vendors(request):
    vendor_detail = UserVendor.objects.all()
    context = {
        'vendors': vendor_detail,
    }
    return render(request, 'adminPanel/showVendor.html', context)

#customers
def show_cust(request):
    cust_detail = UserCustomer.objects.all()
    context = {
        'customers': cust_detail
    }
    return render(request, 'adminPanel/showCust.html', context)

def add_cust(request):
    cust = UserCustomer.objects.all()
    if request.method == 'POST':
        username=request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        confirmpassword = request.POST.get('confirmpassword')
        phone = request.POST.get('phone') 
        address = request.POST.get('address') 
        # if :
        #     messages.success(request,('Passwords match!'))
        #     return redirect('user:signup')
        
        if password != confirmpassword or UserCustomer.objects.filter(email=email).exists():
            messages.success(request,('Email already exists!'))
            return redirect('user:signup')
        else:
            cust = User.objects.create_user(username=username, email=email, password=password)
            cust.save()

            custData = UserCustomer.objects.create(
                username=username,
                name=name,
                email=email,
                password=password,
                phone=phone,
                address=address
            ) 
            custData.save()
            messages.success(request,('Customer Added Successfully!'))
    return render(request, 'adminPanel/addCustomer.html', {"customer":cust})

def update_cust(request, id):
    customer = UserCustomer.objects.get(id= id)
    if request.method == 'POST':
        username=request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        phone = request.POST.get('phone') 
        address = request.POST.get('address') 
        
        customer.username = username
        customer.name = name
        customer.email = email
        customer.password = password
        customer.phone = phone
        customer.address = address
        customer.save()
        return render(request, 'adminPanel/showCust.html', {"customer":customer})
    return render(request, 'adminPanel/updateCust.html', {"customer":customer})

def delete_cust(request, id):
    cust = UserCustomer.objects.get(id=id)
    cust.delete()
    return render(request, 'adminPanel/showCust.html', {"cust":cust})

#bookings
def show_books(request):
    booking_detail = Booking.objects.order_by('date')
    context = {
        'bookings': booking_detail
    }
    return render(request, 'adminPanel/showBook.html', context)
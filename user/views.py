from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth.models import User
from .models import UserCustomer , UserVendor


@csrf_exempt
# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password') 

#         if UserCustomer.objects.filter(email=email).exists():
#             username = UserCustomer.objects.get(email=email).username
#             user = authenticate(request, username=username, password=password)
#         else:
#             messages.info(request, 'Username OR password is incorrect')
#             return redirect('user:login')
        
#         if user is not None:
#             login(request, user)
#             return redirect('venue:home')
#         else:
#             messages.error(request, 'Username OR password is incorrect')
#             return redirect('user:login')

#     return render(request, 'authenticate/login.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                messages.success(request,('You have been logged in!'))
                return redirect('venue:home')
        else:
            messages.success(request,('Error logging in - please try again...'))
    return render(request, 'authenticate/login.html')


def signup_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        confirmpassword = request.POST.get('confirmpassword')
        phone = request.POST.get('phone') 
        address = request.POST.get('address') 
        if password == confirmpassword:
            messages.success(request,('Passwords match!'))
            return redirect('user:signup')
        
        if models.UserCustomer.objects.filter(email=email).exists():
            messages.success(request,('Email already exists!'))
            return redirect('user:signup')
        else:
            customer = User.objects.create_user(username=username, email=email, password=password)
            customer.save()

            UserCustomer.objects.create(
                username=username,
                name=name,
                email=email,
                password=password,
                phone=phone,
                address=address
            )
            messages.success(request,('Account created successfully!'))
            return redirect('user:login')
        
    return render(request, 'authenticate/signup.html')
@csrf_exempt
def login_vendor(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You have been logged in!'))
            return redirect('venue:home')
        else:
            messages.success(request,('Error logging in - please try again...'))
    return render(request, 'authenticate/login.html')


def signup_vendor(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        confirmpassword = request.POST.get('confirmpassword')
        phone = request.POST.get('phone') 
        address = request.POST.get('address') 
        if password == confirmpassword:
            messages.success(request,('Passwords match!'))
            return redirect('user:signup')
        
        if models.UserVendor.objects.filter(email=email).exists():
            messages.success(request,('Email already exists!'))
            return redirect('user:signup')
        else:
            vendor = User.objects.create_user(username=username, email=email, password=password)
            vendor.save()

            UserVendor.objects.create(
                username=username,
                name=name,
                email=email,
                password=password,
                phone=phone,
                address=address
            )
            messages.success(request,('Account created successfully!'))
            return redirect('venue:home')
        
    return render(request, 'authenticate/signup.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect("venue:home")
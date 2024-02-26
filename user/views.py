from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth.models import User
from .models import UserCustomer , UserVendor
import random
from django.contrib import messages
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

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

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        if UserCustomer.objects.filter(username=username):
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['email'] = UserCustomer.objects.get(username=username).email
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
        
        if models.UserCustomer.objects.filter(email=email):
            messages.success(request,('Email already exists!'))
            return redirect('user:signup')
        else:
            customer = User.objects.create_user(username=username, email=email, password=password)
            customer.save()

            cust=UserCustomer.objects.create(
                username=username,
                name=name,
                email=email,
                password=password,
                phone=phone,
                address=address
            )
            cust.save()
            messages.success(request,('Account created successfully!'))
            return redirect('user:login')
    return render(request, 'authenticate/signup.html')

@csrf_exempt
def login_vendor(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        if UserVendor.objects.filter(username=username):
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You have been logged in!'))
            return redirect('vendor:vendor')
        else:
            messages.success(request,('Error logging in - please try again...'))
    return render(request, 'authenticate/login.html' )


def signup_vendor(request):
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
        
        if password != confirmpassword or models.UserVendor.objects.filter(email=email).exists():
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
            messages.success(request,('Account created successfully!'))
            return redirect('vendor:vendor')
        
    return render(request, 'authenticate/signup.html')

@csrf_exempt
def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_exists = UserCustomer.objects.filter(email=email)

        if user_exists:
            user = UserCustomer.objects.get(email=email)
            messages.success(request, 'Email exists!')

            # Generate OTP
            otp = str(random.randint(100000, 999999))

            # Compose the email message
            subject = 'Your OTP for password reset'
            message = f'Your OTP is {otp}.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            # Print for testing, comment out in production
            print(subject, message, from_email, recipient_list)

            # Send the email using Gmail
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            # Store the OTP in the session for later verification
            timestamp = datetime.now().timestamp()  # Current timestamp
            request.session['otp'] = otp
            request.session['otp_timestamp'] = str(timestamp)
            request.session['email'] = email
            return redirect('user:verify_otp')  # Redirect to OTP verification page
        else:
            messages.error(request, 'Email does not exist!')
            return redirect('user:forgetpassword')

    return render(request, 'authenticate/forgetPassword.html')

@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        timestamp = float(request.session['otp_timestamp'])
        current_timestamp = datetime.now().timestamp()
        time_difference = current_timestamp - timestamp
        if time_difference > 300:  # 5 minutes
            messages.error(request, 'OTP expired!')
            return redirect('user:forgetpassword')
        if otp == request.session['otp']:
            return redirect('user:reset_password')
        else:
            messages.error(request, 'Invalid OTP!')
            return redirect('user:verify_otp')
    return render(request, 'authenticate/verifyOtp.html')

@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        print(password, confirm_password)
        if password == confirm_password:
            email = request.session['email']
            user = UserCustomer.objects.get(email=email)
            user.password = password
            authuser = User.objects.get(email=email)
            authuser.set_password(password)
            user.save()
            authuser.save()
            messages.success(request, 'Password reset successfully!')
            return redirect('user:login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('user:reset_password')
    return render(request, 'authenticate/resetPassword.html')


@login_required
def logout_vendor(request):
    logout(request)
    request.session.flush()
    return redirect("venue:home")
    
@login_required
def logoutUser(request):
    logout(request)
    return redirect("venue:home")
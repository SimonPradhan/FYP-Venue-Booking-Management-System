from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@csrf_exempt
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
    
    return render(request, 'authenticate/signup.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect("venue:home")
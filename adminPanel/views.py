from django.shortcuts import render
from user.views import UserVendor

def index(request):
    return render(request, 'adminPanel/index.html', {"name":"name"})

def add_vendor(request):
    vendor = UserVendor.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        addVendor = UserVendor.objects.create(
            username = username,
            name = name,
            password = password,
            email = email, 
            address = address,
            phone = phone
        )
        addVendor.save()
        return render(request, 'adminPanel/showVendor.html')
    return render(request, 'adminPanel/addVendor.html', {"vendor":vendor})

def delete_vendor(request, id):
    vendor = UserVendor.objects.get(id=id)
    vendor.delete()
    return render(request, 'adminPanel/showVendor.html', {"vendor":vendor})

def show_vendors(request):
    vendor_detail = UserVendor.objects.all()
    context = {
        'vendors': vendor_detail
    }
    return render(request, 'adminPanel/showVendor.html', context)

from django.shortcuts import render
from user.models import UserVendor
# Create your views here.
def chat(request):
    return render(request,'chats/chatingPortel.html')

def vendor_list(request):
    vendor_list = UserVendor.objects.all()
    return render(request,'chats/vendor_list.html')
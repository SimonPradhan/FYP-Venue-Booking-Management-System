from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from user.models import UserVendor
# Create your views here.
@login_required
def chat(request):
    return render(request,'chats/chatPortal.html')

def vendor_list(request):
    vendor_list = UserVendor.objects.all()
    return render(request,'chats/vendor_list.html')
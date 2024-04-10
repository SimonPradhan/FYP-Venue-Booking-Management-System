from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from chats.models import Room
from user.models import UserVendor
# Create your views here.
@login_required
def chat(request):
    return render(request,'chatPortal.html')

# def vendor_list(request):
#     vendor_list = UserVendor.objects.all()
#     return render(request,'chats/vendor_list.html')



# def index_view(request):
#     return render(request, 'index.html', {
#         'rooms': Room.objects.all(),
#     })

def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'room.html', {
        'room': chat_room,
    })
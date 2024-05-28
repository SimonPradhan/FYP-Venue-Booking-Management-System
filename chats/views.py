from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from chats.models import Room
from venue.models import Venue
from user.models import UserVendor, UserCustomer
from django.shortcuts import render, get_object_or_404

# Create your views here.
@login_required
def chat(request):
    user = request.user
    print(user)
    vendor_id = user.id
    rooms = Room.objects.filter(vendor_id=vendor_id)
    venue_id = request.GET.get('venue_id')
    user_id = request.GET.get('user_id')
    room = None

    if venue_id and user_id:
        # Check if the provided user_id corresponds to a UserVendor instance
        vendor = get_object_or_404(UserVendor, username=rooms.vendor_id)  # Assuming username is used to identify vendors
        if vendor:
            room = Room.objects.filter(vendor_id=vendor_id)  # Get the first room matching the condition

    return render(request, 'chatPortal.html', {'rooms': rooms, 'room': room, 'venue_id': venue_id, 'user_id': user_id, 'vendor_id': user})




# def vendor_list(request):
#     vendor_list = UserVendor.objects.all()
#     return render(request,'chats/vendor_list.html')



# def index_view(request):
#     return render(request, 'index.html', {
#         'rooms': Room.objects.all(),
#     })

def room_view(request):
    venue_id = request.GET.get('venue_id')
    user_id = request.GET.get('user_id')
    
    try:
        venue = get_object_or_404(Venue, id=venue_id)
        vendor_id = venue.vendor_id
    except Venue.DoesNotExist:
        pass
    
    try:
        user = get_object_or_404(UserCustomer, id=user_id)
    except UserCustomer.DoesNotExist:
        pass

    room_name= str(user.username+vendor_id.username)
    print(room_name)
    # Create or get the chat room
    chat_room, created = Room.objects.get_or_create(name=room_name, vendor_id=vendor_id, user_id=user)

    # Pass the context to the template
    return render(request, 'room.html', {'room': chat_room, 'venue_id': venue_id, 'user_id': user_id})  

def room_viewSecond(request):
    venue_id = request.GET.get('venue_id')
    user_id = request.GET.get('user_id')
    
    try:
        venue = get_object_or_404(Venue, id=venue_id)
        vendor_id = venue.vendor_id
    except Venue.DoesNotExist:
        pass
    
    try:
        user = get_object_or_404(UserCustomer, id=user_id)
    except UserCustomer.DoesNotExist:
        pass

    room_name= str(user.username+vendor_id.username)
    print(room_name)
    # Create or get the chat room
    chat_room, created = Room.objects.get_or_create(name=room_name, vendor_id=vendor_id, user_id=user)

    # Pass the context to the template
    return render(request, 'vendorRoom.html', {'room': chat_room, 'venue_id': venue_id, 'user_id': user_id})  
#  {'room': chat_room, 'venue_id': venue_id, 'user_id': user_id}
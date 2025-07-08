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
    # vendor_id = user.id - 1

    vendor_id = UserVendor.objects.get(username = user).id
    print(vendor_id)
    rooms = Room.objects.filter(vendor_id_id=vendor_id)
    print(rooms)
    venue_id = request.GET.get('venue_id')
    user_id = request.GET.get('user_id')
    
    return render(request, 'chatPortal.html', {'rooms': rooms, 'venue_id': venue_id, 'user_id': user_id, 'vendor_id': user})




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

def room_viewSecond(request, user_id):
    # vendor_id = request.GET.get('vendor_id')
    vendor_id = request.session.get('vendor_id')

    print(vendor_id)
    # user_id = request.GET.get('user_id')
    print(user_id)
    try:
        # Assuming Venue model has a vendor_id field
        vendor_id = get_object_or_404(UserVendor, id=vendor_id)
    except UserVendor.DoesNotExist:
        pass
    
    try:
        user = get_object_or_404(UserCustomer, id=user_id)
    except UserCustomer.DoesNotExist:
        pass

    room_name = str(user.username + vendor_id.username)
    print(room_name)

    chat_room, created = Room.objects.get_or_create(name=room_name, vendor_id=vendor_id, user_id=user)

    return render(request, 'vendorRoom.html', {'room': chat_room, 'user_id': user_id})
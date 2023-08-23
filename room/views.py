from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room, Message
from django.contrib import messages
from .function import slug_create


@login_required
def rooms_view(request):
    """Create room and all Rooms send user."""
    if request.method == "POST":
        room_name = request.POST.get('roomname')
        slug_room = slug_create(room_name.lower())
        print(room_name, slug_room)
        if slug_room:
            room = Room.objects.create(name=room_name, slug=slug_room)
            room.save()
            messages.success(request, f"{room_name} room create.")
        else:
            messages.error(request, f"Room name Empty")
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room_view(request, slug):
    """user ender room slug and this view room all message and user send many message of room."""
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    return render(request, 'room/room.html', {'room': room, "messagess": messages})


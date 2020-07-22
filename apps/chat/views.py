import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': mark_safe(room_name),
        'username': mark_safe(request.user.username)
    })

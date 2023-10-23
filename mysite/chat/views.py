# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import Message
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def home(request):
    return render(request, "home.html")


@login_required
def add_message(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            message = Message(user=request.user, text=text)
            message.save()
    return redirect('home')


def message_list(request):
    messages = Message.objects.all()
    return render(request, 'chat/message_list.html', {'messages': messages})

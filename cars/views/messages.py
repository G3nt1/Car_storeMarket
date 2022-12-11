from cars.models import Messages
from cars.forms import MessageForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def CreateMessages(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['text']
            return redirect('index')

    else:
        form = MessageForm()

    return render(request, 'message.html', {'form': form})


def ShowMessages(request):
    return render(request, 'navbar.html', {'messages':  Messages.objects.filter('received_messages')})

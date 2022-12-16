from cars.forms import MessageForm
from cars.models import Messages, Cars
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect


def Index(request, username=None):
    if username:
        sender = User.objects.filter(username=username).first()

        if not sender:
            return HttpResponseNotFound("Sender not found")

        # mesazhe te cilat na kane ardhur nga sender
        # mesazhet qe ne i kemi derguar senderit
        messages = Messages.objects.filter(Q(sender=sender, recipient=request.user) | Q(sender=request.user, recipient=sender))
    else:
        messages = []

    user_ids = Messages.objects.filter(recipient=request.user).values('sender').distinct()
    bisedat = User.objects.filter(id__in=user_ids)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            # message.recipient = Cars.owner.username
            message.save()
            return redirect('messages_from_user', message.sender.username)
        else:
            return HttpResponseNotFound('Recipient Not Found')

    else:
        form = MessageForm()

    return render(request, 'messages/index.html', {
        "messages": messages,
        "bisedat_user": bisedat,
        "username": username,
        'form': form
    })

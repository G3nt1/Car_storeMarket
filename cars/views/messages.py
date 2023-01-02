from cars.forms import MessageForm
from cars.models import Messages, Cars
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect


# id user, id makine, useragent, ip, daten
def Index(request, username=None):
    if username:
        other_user = User.objects.filter(username=username).first()

        if not other_user:
            return HttpResponseNotFound("User not found")

        # mesazhe te cilat na kane ardhur nga sender
        # mesazhet qe ne i kemi derguar senderit
        messages = Messages.objects \
            .filter(Q(sender=other_user, recipient=request.user) | Q(sender=request.user, recipient=other_user)) \
            .order_by('id')
    else:
        messages = []

    user_ids = Messages.objects.filter(recipient=request.user).values('sender').distinct()
    bisedat = User.objects.filter(id__in=user_ids)
    form = MessageForm()

    return render(request, 'messages/index.html', {
        "messages": messages,
        "bisedat_user": bisedat,
        "username": username,
        'form': form
    })


def SendMessage(request, username):
    recipient = User.objects.filter(username=username).first()

    if not recipient:
        return None  # 404 ketu

    form = MessageForm(request.POST)
    if form.is_valid():
        message = form.save(commit=False)
        message.sender = request.user
        message.recipient = recipient
        message.save()

    return redirect('messages_from_user', username)

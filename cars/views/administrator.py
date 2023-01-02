from cars.models import Cars, CarImage
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# from .decorators import allowed_users


@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
def AdminStatistic(request):
    cars = Cars.objects.all().order_by('-created_date')
    users = User.objects.all()

    return render(request, 'admin/admin_index.html', {'cars': cars, 'users': users})


def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    browser = request.META.get('HTTP_SEC_CH_UA')
    system = request.META.get('HTTP_SEC_CH_UA_PLATFORM')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return render(request, 'admin/ip_monitor.html', {'ip': ip,
                                                     'browser': browser,
                                                     'system': system})

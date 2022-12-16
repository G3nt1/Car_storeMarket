from cars.models import Cars, CarImage
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# from .decorators import allowed_users


@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
def AdminStatistic(request):
    cars = Cars.objects.all()
    users = User.objects.all()

    return render(request, 'admin/admin_index.html', {'cars': cars, 'users': users})



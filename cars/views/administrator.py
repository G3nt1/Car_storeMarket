from cars.models import Cars, Visit
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
    visit = Visit.objects.all()

    return render(request, 'admin/admin_index.html', {'cars': cars, 'users': users, 'visit': visit})

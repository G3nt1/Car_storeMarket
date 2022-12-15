from cars.models import Cars, CarImage
from django.contrib.auth.models import User
from django.shortcuts import render


def AdminStatistic(request):

    return render(request, 'admin/admin_index.html')
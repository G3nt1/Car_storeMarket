from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from .filters import CarsFilter
from .forms import RegCar, RegUsers, CreateUserForm
from .models import Cars, CarImage


# Create your views here.
def Index(request):

    return render(request, 'index.html')


def CarShow(request):
    f = CarsFilter(request.GET, queryset=Cars.objects.all())

    return render(request, 'show.html', {'results': Cars.objects.all(), 'filter': f})


def Search(request):
    search = request.GET.get('query')
    results = []
    error = None

    if len(search) < 3:
        error = 'Your Query is too short'
    else:
        results = Cars.objects.filter(
            Q(brand__icontains=search) |
            Q(model__icontains=search) |
            Q(fuel_type__icontains=search) |
            Q(mileage__icontains=search) |
            Q(year__icontains=search) |
            Q(motor__icontains=search) |
            Q(price__icontains=search) |
            Q(doors__icontains=search) |
            Q(seats__icontains=search) |
            Q(color__icontains=search) |
            Q(features__icontains=search) |
            Q(gearbox__icontains=search)

        )
    context = {
        'results': results,
        'search': search,
        'error': error
    }
    return render(request, 'search.html', context)


@login_required
def RegisterCar(request):
    if request.method == 'POST':
        form = RegCar(request.POST, request.FILES)
        files = request.FILES.getlist("image")
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            for i in files:
                CarImage.objects.create(model=obj, image=i)

            messages.success(request, "New Car Added")
            return redirect('cars')
    form = RegCar()

    return render(request, 'register-car.html', {'form': form})


def CarDetails(request, pk):
    makina = Cars.objects.get(id=pk)

    return render(request, 'car_details.html', {'makinat': makina})


def LoginClient(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars')

    return render(request, 'loginclient.html')


def LogoutClient(request):
    logout(request)
    return redirect('cars')


def RegClients(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        profile_form = RegUsers(request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.username = user
            profile.email = user.email
            profile.phone = request.POST['phone']
            profile.address = request.POST['address']
            profile.city = request.POST['city']
            profile.zip_code = request.POST['zip_code']
            profile.country = request.POST['country']
            profile.save()
            return redirect('login')
    else:
        user_form = CreateUserForm()
        profile_form = RegUsers()
    context = {'user_form': user_form, 'form': profile_form}
    return render(request, 'register.html', context)

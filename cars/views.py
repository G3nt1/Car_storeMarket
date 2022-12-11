from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .filters import CarsFilter
from .forms import RegCar, RegUsers, CreateUserForm
from .models import Cars, CarImage


def get_car_filter(request):
    return CarsFilter(request.GET, queryset=Cars.objects.all().order_by('-created_date'))


def get_current_page_object(request, query_set):
    return Paginator(query_set, per_page=3).get_page(request.GET.get('page'))


def Index(request):
    return render(request, 'index.html')


def CarShow(request):
    return render(request, 'show.html', {
        'search': "",
        'page_obj': get_current_page_object(request, Cars.objects.all()),
        'filter': get_car_filter(request),
    })


def CarAdvancedSearch(request):
    f = get_car_filter(request)

    return render(request, 'show.html', {
        'search': "",
        'page_obj': get_current_page_object(request, f.qs),
        'filter': f,
    })


def CarSearch(request):
    # search from a central search
    search = request.GET.get('query')

    filter_qs = Cars.objects.filter(
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

    return render(request, 'show.html', {
        'search': search,
        'page_obj': get_current_page_object(request, filter_qs),
        'filter': get_car_filter(request),
    })


@login_required
def Register_Car(request):
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


@login_required(login_url='login')
def Update_Car(request, pk):
    car = get_object_or_404(Cars, id=pk)
    if request.user != car.owner:
        return redirect('details', car.pk)
    if request.method == 'POST':
        form = RegCar(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = RegCar(instance=car)

    return render(request, 'update_car.html', {'form': form})


def CarDetails(request, pk):
    makina = Cars.objects.get(id=pk)
    image = CarImage.objects.filter(model=makina)
    return render(request, 'car_details.html', {'makinat': makina, 'image': image})


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

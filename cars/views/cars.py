from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from cars.filters import CarsFilter
from cars.forms import RegCar, RegUsers, CreateUserForm
from cars.models import Cars, CarImage


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

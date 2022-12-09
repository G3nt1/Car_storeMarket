from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.db import models
from django.utils.datetime_safe import datetime, date


class ApplicationUser(models.Model):
    COUNTRY_CHOICES = (
        ("FR", "France"),
        ("DE", "Germany"),
        ("AL", "Albania"),
        ("BE", "Belgium"),
        ("NL", "Nederland"),
        ("IT", "Italy"),
    )
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    address = models.CharField("Address line ", max_length=1024)
    city = models.CharField("City", max_length=1024)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    country = models.CharField(choices=COUNTRY_CHOICES, default='AL', max_length=1040)

    def __str__(self):
        return f'{self.username} {self.city} {self.country}'


class Cars(models.Model):
    CARS_BRANDS = (
        ('bmw', 'BMW'),
        ('mercedes benz', 'Mercedes Benz'),
        ('audi', 'Audi'),
        ('subaru', 'Subaru'),
        ('tesla', 'Tesla'),
        ('jaguar', 'Jaguar'),
        ('land rover', 'Land Rover'),
        ('bentley', 'Bentley'),
        ('bugatti', 'Bugatti'),
        ('ferrari', 'Ferrari'),
        ('lamborghini', 'Lamborghini'),
        ('honda', 'Honda'),
        ('toyota', 'Toyota'),
        ('chevrolet', 'Chevrolet'),
        ('porsche', 'Porsche'),
        ('renault', 'Renault')
    )
    CHOICES_FEATURES = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    CHOICES_FUEL = [
        ('diesel', 'diesel'),
        ('benzina', 'Gasoline'),
        ('electric', 'electric'),
    ]
    CHOICES_GEAR = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]
    number = 10000

    CHOICES_SELLER = [
        ('private', 'Private'),
        ('company', 'Company'),
    ]
    YEAR_CHOICES = [(r, r) for r in range(1984, date.today().year + 1)]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(choices=CARS_BRANDS, max_length=200)
    model = models.CharField(max_length=250)
    fuel_type = models.CharField(max_length=200, choices=CHOICES_FUEL, default='diesel')
    mileage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gearbox = models.CharField(max_length=50, choices=CHOICES_GEAR, null=True, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default='2000')
    motor = models.CharField(max_length=150, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    seller = models.CharField(max_length=200, choices=CHOICES_SELLER, null=True, blank=True)
    doors = models.IntegerField(null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=250, null=True, blank=True)
    features = MultiSelectField(max_length=1000, choices=CHOICES_FEATURES)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    previous_owners = models.IntegerField(null=True, blank=True)
    image = models.FileField(upload_to='static/images-cars/%Y/%m', null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'


class CarImage(models.Model):
    model = models.ForeignKey(Cars, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='static/images-cars/%Y/%m', null=True, blank=True)

    def __str__(self):
        return f'{self.model}'

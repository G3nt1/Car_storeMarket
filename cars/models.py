from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.db import models
from django.utils.datetime_safe import datetime, date


class Cars(models.Model):
    CARS_BRANDS = (
        ('Bmw', 'BMW'),
        ('Mercedes benz', 'Mercedes Benz'),
        ('Audi', 'Audi'),
        ('Subaru', 'Subaru'),
        ('Tesla', 'Tesla'),
        ('Jaguar', 'Jaguar'),
        ('Land rover', 'Land Rover'),
        ('Bentley', 'Bentley'),
        ('Bugatti', 'Bugatti'),
        ('Ferrari', 'Ferrari'),
        ('Lamborghini', 'Lamborghini'),
        ('Honda', 'Honda'),
        ('Toyota', 'Toyota'),
        ('Chevrolet', 'Chevrolet'),
        ('Porsche', 'Porsche'),
        ('Renault', 'Renault')
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
    COUNTRY_CHOICES = (
        ("France", "France"),
        ("Germany", "Germany"),
        ("Albania", "Albania"),
        ("Belgium", "Belgium"),
        ("Nederland", "Nederland"),
        ("Italy", "Italy"),

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
    mileage = models.IntegerField(null=True, blank=True)
    gearbox = models.CharField(max_length=50, choices=CHOICES_GEAR, null=True, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default='2000')
    motor = models.CharField(max_length=150, null=True, blank=True)
    price = models.IntegerField()
    seller = models.CharField(max_length=200, choices=CHOICES_SELLER, null=True, blank=True)
    doors = models.IntegerField(null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=250, null=True, blank=True)
    features = MultiSelectField(max_length=1000, choices=CHOICES_FEATURES)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    previous_owners = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=1024, null=True, blank=True)
    city = models.CharField(max_length=1024, null=True, blank=True)
    zip_code = models.CharField(max_length=12, null=True, blank=True)
    country = models.CharField(choices=COUNTRY_CHOICES, default='AL', max_length=1040)
    image = models.FileField(upload_to='static/images-cars/%Y/%m', null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'


class CarImage(models.Model):
    model = models.ForeignKey(Cars, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='static/images-cars/%Y/%m', null=True, blank=True)

    def __str__(self):
        return f'{self.model}'


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Visit(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ip = models.CharField(max_length=15)
    user_agent = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Cars, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user} {self.car} {self.ip} {self.date}'

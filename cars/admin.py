from django.contrib import admin
from cars.models import Cars, ApplicationUser, CarImage


admin.site.register(Cars)
admin.site.register(ApplicationUser)
admin.site.register(CarImage)

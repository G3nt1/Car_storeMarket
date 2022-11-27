import django_filters
from .models import Cars


class CarsFilter(django_filters.FilterSet):
    class Meta:
        model = Cars
        fields = {'brand': ['exact'], 'model': ['exact'], 'gearbox': ['exact'], 'color': ['exact'],
                  'fuel_type': ['exact'], 'price': ['exact'], }

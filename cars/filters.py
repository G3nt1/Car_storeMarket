import django_filters
from django.template.defaultfilters import format
from .models import Cars


class CarsFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Cars
        fields = {'brand': ['exact'], 'model': ['exact'], 'gearbox': ['exact'], 'color': ['exact'],
                  'fuel_type': ['exact'], }

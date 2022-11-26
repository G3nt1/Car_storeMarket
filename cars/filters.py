import django_filters
from .models import Cars


class CarsFilter(django_filters.FilterSet):
    class Meta:
        model = Cars
        fields = {'brand': ['exact'], 'model': ['contains'], 'gearbox': ['exact'], 'color': ['contains']}

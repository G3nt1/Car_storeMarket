from django.contrib import admin
from cars.models import Cars, CarImage, Monitor


class HitAdmin(admin.ModelAdmin):
    list_display = ('formatted_hit_count',)

    def formatted_hit_count(self, obj):
        return obj.current_hit_count if obj.current_hit_count > 0 else '-'

    formatted_hit_count.admin_order_field = 'hit_count'
    formatted_hit_count.short_description = 'Hits'


admin.site.register(Cars)
admin.site.register(CarImage)
admin.site.register(Monitor)

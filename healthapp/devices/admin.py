from django.contrib import admin

from .models import fda_data, eudamed_data

@admin.register(fda_data)
class FdaDataAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'manufacturer_name')

@admin.register(eudamed_data)
class EudamedDataAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'manufacturer_name')
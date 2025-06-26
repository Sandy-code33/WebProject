from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'latitude', 'longitude', 'timestamp')
    search_fields = ('user_id',)
    list_filter = ('timestamp',)

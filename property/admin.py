from django.contrib import admin
from django.contrib.auth.models import User

from .models import Flat
from .models import Complaint


class Admin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_editable = ['new_building']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


admin.site.register(Flat, Admin)
admin.site.register(Complaint, ComplaintAdmin)
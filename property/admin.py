from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


class Admin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_editable = ['new_building']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['owners_flats']


admin.site.register(Flat, Admin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
from django.contrib import admin
from .models import Property, Inquiry


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'status', 'created_at')
    list_filter = ('status', 'location')
    search_fields = ('title', 'location')


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('property', 'tenant', 'created_at')



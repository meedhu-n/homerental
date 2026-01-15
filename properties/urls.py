from django.urls import path
from . import admin_views
from .views import create_inquiry

urlpatterns = [
    path('admin/properties/', admin_views.admin_property_list, name='admin_property_list'),
    path('admin/properties/<int:property_id>/approve/', admin_views.approve_property, name='approve_property'),
    path('admin/properties/<int:property_id>/reject/', admin_views.reject_property, name='reject_property'),
     path('properties/<int:property_id>/inquire/', create_inquiry, name='create_inquiry'),
]

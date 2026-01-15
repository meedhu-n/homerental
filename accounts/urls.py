from django.urls import path
from .views import role_redirect
from .views import dashboard_redirect

urlpatterns = [
    path('redirect/', role_redirect, name='role_redirect'),
     path("dashboard/", dashboard_redirect, name="dashboard"),
]

from django.contrib import admin
from django.urls import path
from properties.views import tenant_property_list
from properties.views import property_detail
from django.urls import path, include


from properties.views import (
    admin_property_list,
    admin_property_approve,
    admin_property_reject,
    owner_rejected_properties,   
    owner_property_edit,   
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "dashboard/admin/properties/",
        admin_property_list,
        name="admin_property_list",
    ),
    path(
        "dashboard/admin/properties/<int:pk>/approve/",
        admin_property_approve,
        name="admin_property_approve",
    ),
    path(
        "dashboard/admin/properties/<int:pk>/reject/",
        admin_property_reject,
        name="admin_property_reject",
    ),
    path(
    "dashboard/owner/rejected/",
    owner_rejected_properties,
    name="owner_rejected_properties",

    ),
    path(
    "properties/",
    tenant_property_list,
    name="tenant_property_list",
),
    path(
    "properties/<int:pk>/",
    property_detail,
    name="property_detail",
),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),


]
from accounts.views import (
    home,
    admin_dashboard,
    owner_dashboard,
    tenant_dashboard
)

urlpatterns = [
    path('', home, name='home'),

    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/owner/', owner_dashboard, name='owner_dashboard'),
    path('dashboard/tenant/', tenant_dashboard, name='tenant_dashboard'),
]



urlpatterns = [
    path("", include("core.urls")),
    path("properties/", include("properties.urls")),
    path("accounts/", include("accounts.urls")),
]

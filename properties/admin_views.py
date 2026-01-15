from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Property
from .permissions import admin_required

@login_required
def admin_property_list(request):
    admin_required(request.user)

    properties = Property.objects.filter(status__in=['PAID', 'PENDING'])

    output = "\n".join([p.title for p in properties])
    return HttpResponse(output or "No properties pending review")

@login_required
def approve_property(request, property_id):
    admin_required(request.user)

    prop = get_object_or_404(Property, id=property_id)

    if prop.status not in ['PAID', 'PENDING']:
        return HttpResponse("Property cannot be approved")

    prop.status = 'APPROVED'
    prop.rejection_reason = None
    prop.save()

    return HttpResponse("Property approved successfully")

@login_required
def reject_property(request, property_id):
    admin_required(request.user)

    prop = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        reason = request.POST.get('reason')

        if not reason:
            return HttpResponse("Rejection reason is required")

        prop.status = 'REJECTED'
        prop.rejection_reason = reason
        prop.save()

        return HttpResponse("Property rejected")

    return HttpResponse("Send rejection reason via POST")

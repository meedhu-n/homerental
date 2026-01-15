from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Property, Inquiry
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def admin_property_list(request):
    properties = Property.objects.filter(status__in=["PAID", "PENDING"])
    return render(
        request,
        "properties/admin_property_list.html",
        {"properties": properties},
    )


@require_POST
def admin_property_approve(request, pk):
    prop = get_object_or_404(Property, pk=pk)
    prop.status = "APPROVED"
    prop.rejection_reason = ""
    prop.save()
    return redirect("admin_property_list")


@require_POST
def admin_property_reject(request, pk):
    prop = get_object_or_404(Property, pk=pk)
    prop.status = "REJECTED"
    prop.rejection_reason = request.POST.get("reason")
    prop.save()
    return redirect("admin_property_list")

@login_required
def owner_rejected_properties(request):
    properties = Property.objects.filter(
        owner=request.user,
        status="REJECTED"
    )
    return render(
        request,
        "properties/owner_rejected_list.html",
        {"properties": properties},
    )

@login_required
def owner_property_edit(request, pk):
    prop = get_object_or_404(
        Property,
        pk=pk,
        owner=request.user,
        status="REJECTED",
    )

    if request.method == "POST":
        prop.title = request.POST.get("title")
        prop.price = request.POST.get("price")
        prop.description = request.POST.get("description")

        prop.status = "PENDING"
        prop.rejection_reason = ""
        prop.save()

        return redirect("owner_rejected_properties")

    return render(
        request,
        "properties/owner_property_edit.html",
        {"property": prop},
    )

def tenant_property_list(request):
    properties = Property.objects.filter(status="APPROVED")

    location = request.GET.get("location")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    if location:
        properties = properties.filter(location__icontains=location)

    if min_price:
        properties = properties.filter(price__gte=min_price)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    return render(
        request,
        "properties/tenant_property_list.html",
        {"properties": properties},
    )
def property_detail(request, pk):
    property = get_object_or_404(
        Property,
        pk=pk,
        status="APPROVED"
    )
    return render(
        request,
        "properties/property_detail.html",
        {"property": property},
    )

@login_required
def create_inquiry(request, property_id):
    if request.user.role != 'TENANT':
        return redirect('home')

    property_obj = get_object_or_404(Property, id=property_id, status='APPROVED')

    if request.method == 'POST':
        message = request.POST.get('message')
        Inquiry.objects.create(
            property=property_obj,
            tenant=request.user,
            message=message
        )
        return redirect('property_detail', property_id=property_id)


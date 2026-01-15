from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def role_redirect(request):
    user = request.user

    if user.role == 'ADMIN':
        return redirect('/dashboard/admin/')
    elif user.role == 'OWNER':
        return redirect('/dashboard/owner/')
    elif user.role == 'TENANT':
        return redirect('/dashboard/tenant/')
    else:
        return redirect('/')
    
@login_required
def dashboard_redirect(request):
    role = request.user.role

    if role == "ADMIN":
        return redirect("/dashboard/admin/")
    elif role == "OWNER":
        return redirect("/dashboard/owner/")
    else:
        return redirect("/dashboard/tenant/")

def home(request):
    return render(request, "home.html")


@login_required
def dashboard_redirect(request):
    user = request.user

    if user.role == 'ADMIN':
        return redirect('admin_dashboard')
    elif user.role == 'OWNER':
        return redirect('owner_dashboard')
    elif user.role == 'TENANT':
        return redirect('tenant_dashboard')
    
@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


@login_required
def owner_dashboard(request):
    return render(request, 'owner/dashboard.html')


@login_required
def tenant_dashboard(request):
    return render(request, 'tenant/dashboard.html')

@login_required
def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        return redirect('home')
    return render(request, 'admin/dashboard.html')

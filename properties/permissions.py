from django.core.exceptions import PermissionDenied


def admin_required(user):
    if user.role != 'ADMIN':
        raise PermissionDenied("Admin access only")

from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    """
    Requires user membership in at least one of the groups passed.
    """
    def in_groups(u):
        if u.is_authenticated:
            if u.is_superuser or bool(u.groups.filter(name__in=group_names)):
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)

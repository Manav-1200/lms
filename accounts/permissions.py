from rest_framework import permissions

class IsInGroup(permissions.BasePermission):
    """
    Grants access if the user is in any of the allowed groups.
    Usage: permission_classes = [IsInGroup("Admin", "Instructor")]
    """
    def __init__(self, *groups):
        self.groups = groups

    def has_permission(self, request, view):
        user = request.user
        return (
            user and user.is_authenticated and (
                user.is_superuser or user.groups.filter(name__in=self.groups).exists()
            )
        )

def IsAdmin():
    return IsInGroup("Admin")

def IsInstructor():
    return IsInGroup("Instructor")

def IsStudent():
    return IsInGroup("Student")

def IsSponsor():
    return IsInGroup("Sponsor")



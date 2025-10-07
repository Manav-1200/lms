from django.contrib import admin
from django.urls import path, include
from accounts.views import role_redirect, welcome

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", welcome, name="welcome"),
    path("accounts/", include("accounts.urls")),
    path("courses/", include("courses.urls")),
    path("enrollments/", include("enrollments.urls")),
    path("notifications/", include("notifications.urls")),
    path("sponsors/", include("sponsors.urls")),
    path("dashboards/", include("dashboards.urls")),
    path("role-redirect/", role_redirect, name="role_redirect"),
]

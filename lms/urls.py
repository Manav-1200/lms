from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", accounts_views.welcome, name="welcome"),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("courses/", include(("courses.urls", "courses"), namespace="courses")),
    path("enrollments/", include(("enrollments.urls", "enrollments"), namespace="enrollments")),
    path("notifications/", include(("notifications.urls", "notifications"), namespace="notifications")),
]

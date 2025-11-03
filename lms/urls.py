from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.views.generic import RedirectView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # welcome public page
    path('', accounts_views.welcome, name='welcome'),

    # Accounts (for login, logout, profile, register)
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # Courses and sectors
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),

    # Enrollments 
    path('enrollments/', include(('enrollments.urls', 'enrollments'), namespace='enrollments')),

    # Sponsors
    path('sponsors/', include(('sponsors.urls', 'sponsors'), namespace='sponsors')),

    # Notifications
    path('notifications/', include(('notifications.urls', 'notifications'), namespace='notifications')),

    # Dashboards with role-based
    path('dashboards/', include(('dashboards.urls', 'dashboards'), namespace='dashboards')),

    # Simple redirect for root to welcome if necessary
    path('home/', RedirectView.as_view(url='/', permanent=False)),
]

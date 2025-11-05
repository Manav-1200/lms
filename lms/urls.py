from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Welcome public page
    path('', accounts_views.welcome, name='welcome'),

    # Accounts (HTML pages)
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # Courses and sectors (HTML pages)
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),

    # Enrollments (HTML pages)
    path('enrollments/', include(('enrollments.urls', 'enrollments'), namespace='enrollments')),

    # Sponsors (HTML pages)
    path('sponsors/', include(('sponsors.urls', 'sponsors'), namespace='sponsors')),

    # Notifications (HTML pages)
    path('notifications/', include(('notifications.urls', 'notifications'), namespace='notifications')),

    # Dashboards with role-based templates
    path('dashboards/', include(('dashboards.urls', 'dashboards'), namespace='dashboards')),

    # Simple redirect for root to welcome if necessary
    path('home/', RedirectView.as_view(url='/', permanent=False)),

    # ======= REST API Endpoints =======

    # Accounts API
    path('api/accounts/', include(('accounts.urls_api', 'accounts_api'), namespace='accounts_api')),

    # Courses API
    path('api/courses/', include(('courses.urls_api', 'courses_api'), namespace='courses_api')),

    # Enrollments API
    path('api/enrollments/', include(('enrollments.urls_api', 'enrollments_api'), namespace='enrollments_api')),

    # Sponsors API
    path('api/sponsors/', include(('sponsors.urls_api', 'sponsors_api'), namespace='sponsors_api')),

    # Notifications API
    path('api/notifications/', include(('notifications.urls_api', 'notifications_api'), namespace='notifications_api')),

    # Dashboard API
    path('api/dashboards/', include(('dashboards.urls_api', 'dashboards_api'), namespace='dashboards_api')),

    # DRF Spectacular API schema and Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

admin.site.site_header = "Kaptilo"
admin.site.site_title = "Kaptilo"
admin.site.index_title = "Welcome to Kaptilo admin-panel"

urlpatterns = [
    path('', include('apps.core.urls')),
    path("admin/super-sec/", admin.site.urls),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

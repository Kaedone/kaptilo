from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from captcha_admin import admin

admin.autodiscover()

admin.site.site_header = "Kaptilo"
admin.site.site_title = "Kaptilo"
admin.site.index_title = "Welcome to Kaptilo admin-panel"

urlpatterns = [
    path("admin/super-sec/", admin.site.urls),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

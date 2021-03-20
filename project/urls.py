from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import TemplateView

from apps.core import views

admin.site.site_header = "Kaptilo"
admin.site.site_title = "Kaptilo"
admin.site.index_title = "Welcome to Kaptilo admin-panel"

urlpatterns = [
    path('', TemplateView.as_view(template_name="homepage.html"), name="homepage"),
    path('login/', views.login, name="login"),
    path('auth/', views.register, name='auth'),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('create/', views.create_link, name="create_link"),
    path('<int:pk>/', views.follow_link, name='follow_link'),

    path("admin/super-sec/", admin.site.urls),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

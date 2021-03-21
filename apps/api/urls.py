from django.urls import include, path

urlpatterns = [
    path("link", include(("apps.api.link.urls", "apps.api"), namespace="link")),
    path("auth/", include('djoser.urls')),
]

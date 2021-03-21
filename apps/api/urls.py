from django.urls import include, path

urlpatterns = [
    path("", include(("apps.api.link.urls", "apps.api"), namespace="link")),
]

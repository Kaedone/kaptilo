from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("link", views.LinkViewSet, basename="link")

urlpatterns = router.urls

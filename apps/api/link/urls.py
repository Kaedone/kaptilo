from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("", views.LinkViewSet, basename="link")

urlpatterns = router.urls

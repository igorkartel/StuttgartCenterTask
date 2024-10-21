from rest_framework.routers import DefaultRouter

from wildberries.views import ProductViewSet

router = DefaultRouter()

router.register(r"product", ProductViewSet, basename="product")

urlpatterns = router.urls

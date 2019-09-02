from rest_framework import routers
from .viewsets import CatalogViewSet
router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'catalog', CatalogViewSet)

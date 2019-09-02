from rest_framework import viewsets
from rest_framework import permissions
from . import models
from . import serializers

class CatalogViewSet(viewsets.ModelViewSet):
    queryset = models.Catalog.objects.all()
    serializer_class = serializers.CatalogSerializer
    # permiseesion_classes = [permissions.IsAuthenticated]
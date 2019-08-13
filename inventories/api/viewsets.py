from rest_framework.viewsets import ModelViewSet

from inventories.models import Inventory

from .serializers import InventorySerializer


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    http_method_names = ['get']

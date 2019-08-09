from rest_framework.viewsets import ModelViewSet

from inventories.models import Inventory
from zssn.permissions import IsReadOnly

from .serializers import InventorySerializer


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (IsReadOnly,)

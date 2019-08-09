from rest_framework.viewsets import ModelViewSet

from core.models import Survivor
from zssn.permissions import CantDelete, CantUpdate

from .serializers import SurvivorSerializer


class SurvivorViewSet(ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer
    permission_classes = (CantDelete, CantUpdate)

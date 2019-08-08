from rest_framework.viewsets import ModelViewSet

from core.models import Survivor

from .serializers import SurvivorSerializer


class SurvivorViewSet(ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

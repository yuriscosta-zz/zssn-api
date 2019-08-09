from rest_framework.viewsets import ModelViewSet

from flags_infected.models import FlagInfected

from .serializers import FlagInfectedSerializer


class FlagInfectedViewSet(ModelViewSet):
    queryset = FlagInfected.objects.all()
    serializer_class = FlagInfectedSerializer

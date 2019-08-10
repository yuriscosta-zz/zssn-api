from rest_framework.response import Response
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.viewsets import ModelViewSet

from core.models import Survivor

from .serializers import SurvivorSerializer


class SurvivorViewSet(ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'trace']

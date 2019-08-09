from rest_framework.serializers import ModelSerializer

from flags_infected.models import FlagInfected


class FlagInfectedSerializer(ModelSerializer):
    class Meta:
        model = FlagInfected
        fields = '__all__'

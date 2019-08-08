from rest_framework.serializers import ModelSerializer

from core.models import Survivor
from locations.models import Location

from locations.api.serializers import LocationSerializer


class SurvivorSerializer(ModelSerializer):
    last_location = LocationSerializer(many=False)

    class Meta:
        model = Survivor
        fields = '__all__'

    def create_location(self, last_location, survivor):
        new_location = Location.objects.create(**last_location)
        survivor.last_location = new_location

    def update_location(self, last_location, survivor):
        new_location = Location.objects.filter(
            id=survivor.last_location.id
        ).update(**last_location)
    
        survivor.last_location = Location.objects.get(id=new_location)

    def create(self, validated_data):
        last_location = validated_data['last_location']
        del validated_data['last_location']

        survivor = Survivor.objects.create(**validated_data)

        self.create_location(last_location, survivor)

        survivor.save()

        return survivor

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.infected_reports = validated_data.get('infected_reports',
                                                       instance.infected_reports)
        instance.is_infected = validated_data.get('is_infected',
                                                  instance.is_infected)

        location = validated_data['last_location']
        del validated_data['last_location']

        if instance.last_location:
            self.update_location(location, instance)
        else:
            self.create_location(location, instance)

        instance.save()

        return instance

from rest_framework.response import Response
from rest_framework.serializers import Serializer, ModelSerializer, IntegerField
from core.models import Survivor
from locations.models import Location
from inventories.models import Inventory

from locations.api.serializers import LocationSerializer
from inventories.api.serializers import InventorySerializer


class SurvivorSerializer(ModelSerializer):
    last_location = LocationSerializer(many=False, required=False)
    inventory = InventorySerializer(many=False, required=False)

    class Meta:
        model = Survivor
        fields = '__all__'

    def create_location(self, last_location, survivor):
        new_location = Location.objects.create(**last_location)
        survivor.last_location = new_location

    def create_inventory(self, inventory, survivor):
        new_inventory = Inventory.objects.create(**inventory)
        survivor.inventory = new_inventory

    def create(self, validated_data):
        last_location = {}
        if 'last_location' in validated_data.keys():
            last_location = validated_data['last_location']
            del validated_data['last_location']

        inventory = {}
        if 'inventory' in validated_data.keys():
            inventory = validated_data['inventory']
            del validated_data['inventory']

        survivor = Survivor.objects.create(**validated_data)

        self.create_location(last_location, survivor)
        self.create_inventory(inventory, survivor)

        survivor.save()

        return survivor


class TradeSerializer(Serializer):
    sender = IntegerField()
    receiver = IntegerField()
    sender_water = IntegerField()
    sender_food = IntegerField()
    sender_medication = IntegerField()
    sender_ammunition = IntegerField()
    receiver_water = IntegerField()
    receiver_food = IntegerField()
    receiver_medication = IntegerField()
    receiver_ammunition = IntegerField()

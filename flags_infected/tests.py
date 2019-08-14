import json

from rest_framework.test import APITestCase, APIClient
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_405_METHOD_NOT_ALLOWED)

from model_mommy import mommy

from .models import Survivor
from locations.models import Location
from inventories.models import Inventory


class FlagSurvivorTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.location = Location.objects.create(latitude=000000,
                                                longitude=1111111)
        self.location.save()

        self.first_inventory = Inventory.objects.create(water=1,
                                                        food=0,
                                                        medication=0,
                                                        ammunition=0)
        self.second_inventory = Inventory.objects.create(water=0,
                                                         food=0,
                                                         medication=2,
                                                         ammunition=0)
        self.first_inventory.save()
        self.second_inventory.save()

        self.first_survivor = Survivor.objects.create(name="Hans",
                                                      age=75,
                                                      gender="M",
                                                      infected_reports=0,
                                                      last_location=self.location,
                                                      inventory=self.first_inventory)
        self.second_survivor = Survivor.objects.create(name="Murray",
                                                       age=95,
                                                       gender="M",
                                                       infected_reports=0,
                                                       last_location=self.location,
                                                       inventory=self.second_inventory)

        self.first_survivor.save()
        self.second_survivor.save()

        self.first_survivor = Survivor.objects.filter(id=1).first()
        self.second_survivor = Survivor.objects.filter(id=2).first()

    def test_flag_survivor(self):
        data = {
            "author": 1,
            "target": 2
        }

        response = self.client.post('/flag-survivor/',
                                    data=data,
                                    format='json')

        self.assertEqual(response.status_code, HTTP_201_CREATED)

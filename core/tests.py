import json

from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_405_METHOD_NOT_ALLOWED)

from model_mommy import mommy

from .models import Survivor
from locations.models import Location
from inventories.models import Inventory


class SurvivorTestCase(APITestCase):
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

    def test_create_survivor(self):
        data = {
            "last_location": {
                "latitude": 300611.5,
                "longitude": 300744.5
            },
            "inventory": {
                "water": 1,
                "food": 3,
                "medication": 2,
                "ammunition": 3
            },
            "name": "Andi Deris",
            "age": 54,
            "gender": "M",
            "infected_reports": 0
        }

        response = self.client.post('/survivors/',
                                    data=data,
                                    format='json')

        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_create_survivor_without_location(self):
        data = {
            "inventory": {
                "water": 0,
                "food": 1,
                "medication": 1,
                "ammunition": 2
            },
            "name": "Michael Kiske",
            "age": 51,
            "gender": "M",
            "infected_reports": 0
        }

        response = self.client.post('/survivors/',
                                    data=data,
                                    format='json')

        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_create_survivor_without_inventory(self):
        data = {
            "last_location": {
                "latitude": 300611.5,
                "longitude": 300744.5
            },
            "name": "Michael Weikath",
            "age": 57,
            "gender": "M",
            "infected_reports": 0
        }

        response = self.client.post('/survivors/',
                                    data=data,
                                    format='json')

        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_detail_survivor(self):
        response = self.client.get(
            '/survivors/{}/'.format(self.first_survivor.id)
        )
        data = response.json()

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(data['id'], 1)

    def test_list_survivor(self):
        response = self.client.get('/survivors/')
        data = response.json()

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(data), 2)


class TradeTestCase(APITestCase):
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
        self.third_survivor = Survivor.objects.create(name="Stephan",
                                                      age=50,
                                                      gender="M",
                                                      infected_reports=4,
                                                      last_location=self.location,
                                                      inventory=self.second_inventory)

        self.first_survivor.save()
        self.second_survivor.save()
        self.third_survivor.save()

        self.first_survivor = Survivor.objects.filter(id=1).first()
        self.second_survivor = Survivor.objects.filter(id=2).first()
        self.third_survivor = Survivor.objects.filter(id=3).first()

    def test_create_trade(self):
        data = {
            "sender": 1,
            "receiver": 2,
            "sender_water": 1,
            "sender_food": 0,
            "sender_medication": 0,
            "sender_ammunition": 0,
            "receiver_water": 0,
            "receiver_food": 0,
            "receiver_medication": 2,
            "receiver_ammunition": 0
        }

        response = self.client.post('/trade/', data=data, format='json')

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(self.first_survivor.inventory.water, 0)
        self.assertEqual(self.first_survivor.inventory.medication, 2)
        self.assertEqual(self.second_survivor.inventory.water, 1)
        self.assertEqual(self.second_survivor.inventory.medication, 0)

    def test_create_trade_with_differents_points_value(self):
        data = {
            "sender": 1,
            "receiver": 2,
            "sender_water": 1,
            "sender_food": 0,
            "sender_medication": 0,
            "sender_ammunition": 0,
            "receiver_water": 0,
            "receiver_food": 0,
            "receiver_medication": 1,
            "receiver_ammunition": 0
        }

        response = self.client.post('/trade/', data=data, format='json')

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_create_trade_with_infected_survivor(self):
        data = {
            "sender": 1,
            "receiver": 3,
            "sender_water": 1,
            "sender_food": 0,
            "sender_medication": 0,
            "sender_ammunition": 0,
            "receiver_water": 0,
            "receiver_food": 0,
            "receiver_medication": 2,
            "receiver_ammunition": 0
        }

        response = self.client.post('/trade/', data=data, format='json')

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_create_trade_with_inexistent_survivor(self):
        data = {
            "sender": 1,
            "receiver": 4,
            "sender_water": 1,
            "sender_food": 0,
            "sender_medication": 0,
            "sender_ammunition": 0,
            "receiver_water": 0,
            "receiver_food": 0,
            "receiver_medication": 1,
            "receiver_ammunition": 0
        }

        response = self.client.post('/trade/', data=data, format='json')

        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_create_trade_with_more_items_than_the_survivor_had(self):
        data = {
            "sender": 1,
            "receiver": 2,
            "sender_water": 1,
            "sender_food": 0,
            "sender_medication": 0,
            "sender_ammunition": 0,
            "receiver_water": 0,
            "receiver_food": 0,
            "receiver_medication": 0,
            "receiver_ammunition": 4
        }

        response = self.client.post('/trade/', data=data, format='json')

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)


class ReportTestCase(APITestCase):
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
        self.third_survivor = Survivor.objects.create(name="Stephan",
                                                      age=50,
                                                      gender="M",
                                                      infected_reports=4,
                                                      last_location=self.location,
                                                      inventory=self.second_inventory)

        self.first_survivor.save()
        self.second_survivor.save()
        self.third_survivor.save()

        self.first_survivor = Survivor.objects.filter(id=1).first()
        self.second_survivor = Survivor.objects.filter(id=2).first()
        self.third_survivor = Survivor.objects.filter(id=3).first()

    def test_list_reports(self):
        response = self.client.get('/reports/')
        data = response.json()
        expected_data = {
            "water": 0.5,
            "food": 0.0,
            "medication": 1.0,
            "ammunition": 0.0
        }

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(data[0]['value'], '66.67%')
        self.assertEqual(data[1]['value'], '33.33%')
        self.assertEqual(data[2]['value'], 4)
        self.assertAlmostEqual(data[3]['value'], expected_data)

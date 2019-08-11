from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST

from core.models import Survivor
from inventories.models import Inventory

from .serializers import SurvivorSerializer, TradeSerializer


class SurvivorViewSet(ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'trace']


class TradeViewSet(ModelViewSet):
    serializer_class = TradeSerializer
    http_method_names = ['post']

    def validate_survivor(self, id):
        survivor = Survivor.objects.filter(id=id).first()

        return survivor if survivor else False

    def calculate_points(self, water, food, medication, ammunition):
        return int(water) * 4 + int(food) * 3 + int(medication) * 2 + int(ammunition) * 1

    def are_points_equal(self, data):
        sender_points = self.calculate_points(data['sender_water'],
                                              data['sender_food'],
                                              data['sender_medication'],
                                              data['sender_ammunition'])
        receiver_points = self.calculate_points(data['receiver_water'],
                                                data['receiver_food'],
                                                data['receiver_medication'],
                                                data['receiver_ammunition'])

        return sender_points == receiver_points

        def validate_trade_components(self, survivor, data):
            pass

    def create(self, request, pk=None):
        trade = TradeSerializer(data=request.data)
        if trade.is_valid():
            sender = self.validate_survivor(trade.data['sender'])
            receiver = self.validate_survivor(trade.data['receiver'])

            if sender and receiver:
                if sender.is_infected or receiver.is_infected:
                    return Response({'error': "Infected survivors can't trade."},
                                    status=HTTP_400_BAD_REQUEST)

                if not self.are_points_equal(trade.data):
                    return Response({'error': "The points must be equal."},
                                    status=HTTP_400_BAD_REQUEST)

                return Response({'details': 'Ok'},
                                status=HTTP_200_OK)

            return Response({'error': 'One of the survivors was not found.'},
                            status=HTTP_404_NOT_FOUND)

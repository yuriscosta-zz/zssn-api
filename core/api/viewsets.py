from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST

from core.models import Survivor
from inventories.models import Inventory

from .serializers import SurvivorSerializer, TradeSerializer
from .utils import (are_points_equal,
                    are_trade_components_valid,
                    calculate_points,
                    trade_items,
                    validate_survivor,
                    generate_infected_survivors_report,
                    generate_points_lost_report,
                    generate_resources_average_by_survivor_report)


class SurvivorViewSet(ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'trace', 'delete']


class TradeViewSet(ModelViewSet):
    serializer_class = TradeSerializer
    http_method_names = ['post']

    def create(self, request, pk=None):
        trade = TradeSerializer(data=request.data)
        if trade.is_valid():
            sender = validate_survivor(trade.data['sender'])
            receiver = validate_survivor(trade.data['receiver'])

            if sender and receiver:
                if sender.is_infected or receiver.is_infected:
                    return Response({'error': "Infected survivors can't trade."},
                                    status=HTTP_400_BAD_REQUEST)

                if not are_points_equal(trade.data):
                    return Response({'error': "The points must be equal."},
                                    status=HTTP_400_BAD_REQUEST)

                if not are_trade_components_valid(sender, receiver, trade.data):
                    return Response({'error': "The number of items must be equal or less to the items in inventory."},
                                    status=HTTP_400_BAD_REQUEST)

                trade_items(sender, receiver, trade.data)
                return Response({'details': 'Ok'},
                                status=HTTP_200_OK)

            return Response({'error': 'One of the survivors was not found.'},
                            status=HTTP_404_NOT_FOUND)


class ReportViewSet(ViewSet):
    http_method_names = ['get']

    def list(self, request):
        return Response([generate_infected_survivors_report(),
                         generate_infected_survivors_report(is_infected=True),
                         generate_points_lost_report(),
                         generate_resources_average_by_survivor_report()],
                        status=HTTP_200_OK)

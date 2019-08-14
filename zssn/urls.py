from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include

from rest_framework import routers

from core.api.viewsets import SurvivorViewSet, TradeViewSet, ReportViewSet
from locations.api.viewsets import LocationViewSet
from flags_infected.api.viewsets import FlagInfectedViewSet
from inventories.api.viewsets import InventoryViewSet

router = routers.DefaultRouter()
router.register('survivors', SurvivorViewSet)
router.register('locations', LocationViewSet)
router.register('flag-survivor', FlagInfectedViewSet)
router.register('inventories', InventoryViewSet)
router.register('trade', TradeViewSet, base_name='trades')
router.register('reports', ReportViewSet, base_name='reports')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

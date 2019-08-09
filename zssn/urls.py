from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include

from rest_framework import routers

from core.api.viewsets import SurvivorViewSet
from locations.api.viewsets import LocationViewSet
from flags_infected.api.viewsets import FlagInfectedViewSet

router = routers.DefaultRouter()
router.register(r'survivors', SurvivorViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'flags', FlagInfectedViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

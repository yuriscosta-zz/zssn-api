from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include

from rest_framework import routers

from core.api.viewsets import SurvivorViewSet
from locations.api.viewsets import LocationViewSet

router = routers.DefaultRouter()
router.register(r'survivors', SurvivorViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

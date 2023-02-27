from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("buildings", BuildingViewSet)
router.register("coordinates", BuildingViewSet)
router.register("routes", BuildingViewSet)
router.register("rooms", BuildingViewSet)

app_name = "armap"

urlpatterns = [
    path("", include(router.urls))
]
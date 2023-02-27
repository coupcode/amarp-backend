from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from armap.models.building import Building
from armap.models.coordinate import Coordinate
from armap.models.route import Route
from armap.models.room import Room


class BuildingViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"

class CoordinateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"

class RouteViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"

class RoomViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"
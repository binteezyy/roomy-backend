from django.shortcuts import render
from rest_framework import viewsets
from ..models import *
from ..serializers import *

class PropertyApiView(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class RoomApiView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class FeeApiView(viewsets.ModelViewSet):
    queryset = Fee.objects.filter(fee_type=1)
    serializer_class = FeeSerializer
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

class BillingApiView(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

class MessageApiView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class TenantAccountApiView(viewsets.ModelViewSet):
    queryset = TenantAccount.objects.all()
    serializer_class = TenantAccountSerializer

class GuestApiView(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class ImageFileApiView(viewsets.ModelViewSet):
    queryset = ImageFile.objects.all()
    serializer_class = ImageFileSerializer
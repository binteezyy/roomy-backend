from django.shortcuts import render
from rest_framework import viewsets
from ..models import *
from ..serializers import *

class PropertyApiView(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class RoomsByPropertyApiView(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = RoomsByPropertySerializer

class RoomApiView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class FeeApiView(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
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

class TransactionApiView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class RequestApiView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class OwnerAccountApiView(viewsets.ModelViewSet):
    queryset = OwnerAccount.objects.all()
    serializer_class = OwnerAccountSerializer

class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
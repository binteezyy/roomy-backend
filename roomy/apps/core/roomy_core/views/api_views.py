from django.shortcuts import render
from rest_framework import viewsets
from ..models import *
from ..serializers import *
from django.db.models import Q

class PropertyApiView(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class RoomCatalogApiView(viewsets.ModelViewSet):
    queryset = RoomCatalog.objects.all()
    serializer_class = RoomCatalogSerializer

class RoomApiView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSeralizer
    
class FeeApiView(viewsets.ModelViewSet):
    queryset = Fee.objects.filter()
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

class OwnerAccountApiView(viewsets.ModelViewSet):
    queryset = OwnerAccount.objects.all()
    serializer_class = OwnerAccountSerializer

class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TransactionApiView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerliazer

class RequestApiView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class MessageApiView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


## filtered api view
class RoomCatalogInPropertyApiView(viewsets.ModelViewSet):
    serializer_class = RoomCatalogSerializer

    def get_queryset(self):
        user = self.request.user
        rooms = None
        
        rooms = RoomCatalog.objects.filter(property_id=self.kwargs['property_id'])

        return rooms

class RoomCatalogInLocationApiView(viewsets.ModelViewSet):
    serializer_class = RoomCatalogSerializer

    def get_queryset(self):
        user = self.request.user
        rooms = None
        rooms = RoomCatalog.objects.filter(property_id__property_address__icontains=self.kwargs['location'])

        return rooms

class RoomCatalogFilterApiView(viewsets.ModelViewSet):
    serializer_class = RoomCatalogSerializer
    

    def get_queryset(self):
        property_type_enum = (
            (0, 'Condomenium'),
            (1, 'Dormitory'),
            (2, 'Apartment'),
        )
        property_type_reverse = dict((v,k) for k,v in property_type_enum if self.kwargs['search_query'] in v)
        # print(property_type_reverse)
        try:
            pkey = property_type_reverse.values()
            # print(pkey)
        except:
            print("except")
        user = self.request.user

        rooms = RoomCatalog.objects.filter(Q(property_id__name__icontains=self.kwargs['search_query']) | Q(property_id__property_address__icontains=self.kwargs['search_query']) | Q(property_id__property_type__in=pkey))

        return rooms
from rest_framework import serializers
from .models import *

class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'url', 'property_type', 'name', 'description', 'property_address', 'property_image' )

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'url', 'property_id', 'description', 'floor', 'number', 'rate', 'room_type', 'image_3d', 'image_2d')

class FeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fee
        fields = ('id', 'url', 'property_id', 'description', 'amount')

class BillingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Billing 
        fields = ('id', 'url', 'transaction_id', 'time_stamp', 'billing_fee', 'paid')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message 
        fields = ('id', 'url', 'user_id', 'title', 'body', 'time_stamp', 'read')

class TenantAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TenantAccount 
        fields = ('id', 'url', 'user_id', 'birthday', 'cell_number', 'provincial_address')

class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest 
        fields = ('id', 'url', 'transaction_id', 'name', 'time_stamp', 'inside')

class ImageFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageFile
        fields = ('id', 'url', 'title', 'img_path')
from rest_framework import serializers
from .models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'property_type', 'name', 'description', 'property_address', 'property_image' )

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'property_id', 'description', 'floor', 'number', 'rate', 'room_type', 'image_3d', 'image_2d')

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = ('id', 'property_id', 'description', 'amount')

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing 
        fields = ('id', 'transaction_id', 'time_stamp', 'billing_fee', 'paid')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message 
        fields = ('id', 'user_id', 'title', 'body', 'time_stamp', 'read')

class TenantAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantAccount 
        fields = ('id', 'user_id', 'birthday', 'cell_number', 'provincial_address')

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest 
        fields = ('id', 'transaction_id', 'name', 'time_stamp', 'inside')

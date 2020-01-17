from rest_framework import serializers
from .models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('property_type', 'name', 'description', 'property_address', 'property_image' )

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('description', 'floor', 'number', 'rate', 'room_type', 'image_3d', 'image_2d')

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = ('description', 'amount')

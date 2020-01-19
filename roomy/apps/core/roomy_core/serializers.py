from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'url', 'property_type', 'name', 'description', 'property_address', 'property_image', 'rooms_with_this_property')
        depth = 1

class RoomsByPropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'url', 'rooms_with_this_property')


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'url', 'property_id', 'description', 'floor', 'number', 'rate', 'room_type', 'image_3d', 'image_2d', 'transactions_with_this_room')


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


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'url', 'active', 'start_date', 'room_id', 'rating', 'rating_description', 'rated', 'add_ons')


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'url', 'subject', 'description', 'time_stamp', 'status')


class OwnerAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OwnerAccount
        fields = ('id', 'url', 'user_id', 'birthday', 'cell_number', 'provincial_address')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name')
from bootstrap_modal_forms.forms import BSModalForm
from django.shortcuts import render, redirect
from apps.core.roomy_core.models import *
from django import forms

class BillingModalForm(BSModalForm):
    class Meta:
        model = Billing
        exclude = ['transaction_id', 'time_stamp']


class FeeModalForm(BSModalForm):
    class Meta:
        model = Fee
        exclude = ['']

class FeeModelForm(forms.ModelForm):
    class Meta:
        model = Fee
        exclude = ['']


class TransactionModalForm(BSModalForm):
    class Meta:
        model = Transaction
        exclude = ['room_id', 'rating', 'rating_description', 'rated']


class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ['time_stamp']

class ExpenseModalForm(BSModalForm):
    class Meta:
        model = Expense
        exclude = ['time_stamp']

class GuestModalForm(BSModalForm):
    class Meta:
        model = Guest
        exclude = ['']


class RequestModalForm(BSModalForm):
    class Meta:
        model = Request
        exclude = ['transaction_id']

class RequestUpdateModalForm(BSModalForm):
    class Meta:
        model = Request
        fields = ['status',]


class NotifModalForm(BSModalForm):
    class Meta:
        model = Message
        exclude = ['']


class NotifCreateModalForm(BSModalForm):

    class Meta:
        model = Message
        exclude = ['sent']


class BookingModalForm(BSModalForm):
    class Meta:
        model = Booking
        fields = ['status', 'start_date']

class PropertyModelForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['property_image', ]

class PropertyModalForm(BSModalForm):
    class Meta:
        model = Property
        exclude = ['property_image', ]

class RoomCatalogModalForm(BSModalForm):
    class Meta:
        model = RoomCatalog
        exclude = ['img_2d', 'img_3d']

class CatalogModelForm(forms.ModelForm):
    class Meta:
        model = RoomCatalog
        exclude = ['img_2d', 'img_3d']

class RoomModalForm(BSModalForm):
    class Meta:
        model = Room
        exclude = ['catalog_id', 'status']

class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ['',]

class OnotifModalForm(BSModalForm):
    class Meta:
        model = OwnerNotification
        fields = ['read', ]

class AdminAccModalForm(BSModalForm):
    class Meta:
        model = OwnerAccount
        exclude = ['transaction_id', 'user_id']

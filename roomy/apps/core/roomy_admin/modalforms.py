from bootstrap_modal_forms.forms import BSModalForm
from django.shortcuts import render, redirect
from apps.core.roomy_core.models import *


class BillingModalForm(BSModalForm):
    class Meta:
        model = Billing
        exclude = ['transaction_id', ]


class FeeModalForm(BSModalForm):
    class Meta:
        model = Fee
        exclude = ['']


class TransactionModalForm(BSModalForm):
    class Meta:
        model = Transaction
        exclude = ['room_id', 'rating', 'rating_description', 'rated']


class ExpenseModalForm(BSModalForm):
    class Meta:
        model = Expense
        exclude = ['']


class GuestModalForm(BSModalForm):
    class Meta:
        model = Guest
        exclude = ['']


class RequestModalForm(BSModalForm):
    class Meta:
        model = Request
        exclude = ['transaction_id']


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
        fields = ['approved',]


class PropertyModalForm(BSModalForm):
    class Meta:
        model = Property
        exclude = ['property_image', ]

class RoomCatalogModalForm(BSModalForm):
    class Meta:
        model = RoomCatalog
        exclude = ['img_2d', 'img_3d']

class RoomModalForm(BSModalForm):
    class Meta:
        model = Room
        exclude = ['',]


class AdminAccModalForm(BSModalForm):
    class Meta:
        model = OwnerAccount
        exclude = ['transaction_id', 'user_id']

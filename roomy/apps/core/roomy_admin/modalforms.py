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
        exclude = ['room_id']


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
        exclude = ['']

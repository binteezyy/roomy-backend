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

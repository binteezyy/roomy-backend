from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # get_object_or_404, redirect, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views import generic
from django.contrib import messages
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from apps.core.roomy_core.models import *
from apps.core.roomy_admin.modalforms import *


# LoginRequiredMixin, UserPassesTestMixin,
class BillingReadModal(BSModalReadView):
    model = Billing
    context_object_name = 'billing'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        fee_objects = kwargs['object'].billing_fee.all()
        fees = 0
        for fee_object in fee_objects:
            fees += int(fee_object.amount)
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'billing'
        context['billing'] = kwargs['object']
        context['tenants'] = UserAccount.objects.filter(
            transaction_id=kwargs['object'].transaction_id)
        context['fees'] = kwargs['object'].billing_fee.all()
        context['total'] = fees
        return context
    # def test_func(self):
    #     return self.request.user.is_superuser


class BillingDeleteModal(BSModalDeleteView):
    model = Billing
    context_object_name = 'billing'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Billing deleted'
    success_url = reverse_lazy('billing')
    # def test_func(self):
    #     return self.request.user.is_superuser


class BillingUpdateModal(BSModalUpdateView):
    model = Billing
    template_name = 'components/modals/update.html'
    form_class = BillingModalForm
    sucess_message = "Success: Billing updated"
    success_url = reverse_lazy('billing')


class FeeDeleteModal(BSModalDeleteView):
    model = Fee
    context_object_name = 'fee'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Fee deleted'
    success_url = reverse_lazy('fee')
    # def test_func(self):
    #     return self.request.user.is_superuser


class FeeUpdateModal(BSModalUpdateView):
    model = Fee
    template_name = 'components/modals/update.html'
    form_class = FeeModalForm
    sucess_message = "Success: Fee updated"
    success_url = reverse_lazy('fee')

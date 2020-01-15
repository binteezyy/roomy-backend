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


class FeeCreateModal(BSModalCreateView):
    model = Fee
    model_type = 'fee'
    template_name = 'components/modals/create.html'
    form_class = FeeModalForm
    success_message = 'Success: Fee created.'
    success_url = reverse_lazy('fee')

    # def test_func(self):
    #     return self.request.user.is_superuser


class RentalReadModal(BSModalReadView):
    model = Transaction
    context_object_name = 'transaction'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'transaction'
        context['transaction'] = kwargs['object']
        context['room'] = f"Floor-{kwargs['object'].room_id.floor} Number-{kwargs['object'].room_id.number}"
        context['tenants'] = UserAccount.objects.filter(
            transaction_id=kwargs['object'])

        return context
    # def test_func(self):
    #     return self.request.user.is_superuser


class RentalDeleteModal(BSModalDeleteView):
    model = Transaction
    context_object_name = 'transaction'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Transaction deleted'
    success_url = reverse_lazy('rental')
    # def test_func(self):
    #     return self.request.user.is_superuser


class RentalUpdateModal(BSModalUpdateView):
    model = Transaction
    template_name = 'components/modals/update.html'
    form_class = TransactionModalForm
    sucess_message = "Success: Transaction updated"
    success_url = reverse_lazy('rental')


class TenantReadModal(BSModalReadView):
    model = UserAccount
    context_object_name = 'tenants'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'tenants'
        context['tenant'] = kwargs['object']
        context['transaction'] = kwargs['object'].transaction_id
        context['room'] = f"Floor-{kwargs['object']} Number-{kwargs['object'].transaction_id.room_id.number}"

        return context
    # def test_func(self):
    #     return self.request.user.is_superuser


class ExpenseCreateModal(BSModalCreateView):
    model = Expense
    model_type = 'expense'
    template_name = 'components/modals/create.html'
    form_class = ExpenseModalForm
    success_message = 'Success: Expense created.'
    success_url = reverse_lazy('expense')

    # def test_func(self):
    #     return self.request.user.is_superuser


class ExpenseDeleteModal(BSModalDeleteView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Expense deleted'
    success_url = reverse_lazy('expense')
    # def test_func(self):
    #     return self.request.user.is_superuser


class ExpenseUpdateModal(BSModalUpdateView):
    model = Expense
    template_name = 'components/modals/update.html'
    form_class = ExpenseModalForm
    sucess_message = "Success: Expense updated"
    success_url = reverse_lazy('expense')

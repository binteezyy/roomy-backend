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
        context['tenants'] = TenantAccount.objects.filter(
            transaction_id=kwargs['object'].transaction_id)
        context['fees'] = kwargs['object'].billing_fee.all()
        context['total'] = fees
        return context

    def test_func(self):
        return self.request.user.is_staff


class BillingDeleteModal(BSModalDeleteView):
    model = Billing
    context_object_name = 'billing'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Billing deleted'
    success_url = reverse_lazy('billing')

    def test_func(self):
        return self.request.user.is_staff


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

    def test_func(self):
        return self.request.user.is_staff


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

    def test_func(self):
        return self.request.user.is_staff


class RentalReadModal(BSModalReadView):
    model = Transaction
    context_object_name = 'transaction'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        fee_objects = kwargs['object'].add_ons.all()
        fees = int(kwargs['object'].room_id.rate)
        for fee_object in fee_objects:
            fees += int(fee_object.amount)
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'transaction'
        context['transaction'] = kwargs['object']
        context['room'] = f"Floor-{kwargs['object'].room_id.floor} Number-{kwargs['object'].room_id.number}"
        context['tenants'] = TenantAccount.objects.filter(
            transaction_id=kwargs['object'])
        context['add_ons'] = kwargs['object'].add_ons.all()
        context['total'] = fees
        context['rate'] = int(kwargs['object'].room_id.rate)

        return context

    def test_func(self):
        return self.request.user.is_staff


class RentalDeleteModal(BSModalDeleteView):
    model = Transaction
    context_object_name = 'transaction'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Transaction deleted'
    success_url = reverse_lazy('rental')

    def test_func(self):
        return self.request.user.is_staff


class RentalUpdateModal(BSModalUpdateView):
    model = Transaction
    template_name = 'components/modals/update.html'
    form_class = TransactionModalForm
    sucess_message = "Success: Transaction updated"
    success_url = reverse_lazy('rental')


class TenantReadModal(BSModalReadView):
    model = TenantAccount
    context_object_name = 'tenants'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'tenants'
        context['tenant'] = kwargs['object']
        context['transaction'] = kwargs['object'].transaction_id
        context['birthday'] = kwargs['object'].birthday.strftime("%B %d, %Y")

        return context

    def test_func(self):
        return self.request.user.is_staff


class ExpenseCreateModal(BSModalCreateView):
    model = Expense
    model_type = 'expense'
    template_name = 'components/modals/create.html'
    form_class = ExpenseModalForm
    success_message = 'Success: Expense created.'
    success_url = reverse_lazy('expense')

    def test_func(self):
        return self.request.user.is_staff


class ExpenseDeleteModal(BSModalDeleteView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Expense deleted'
    success_url = reverse_lazy('expense')

    def test_func(self):
        return self.request.user.is_staff


class ExpenseUpdateModal(BSModalUpdateView):
    model = Expense
    template_name = 'components/modals/update.html'
    form_class = ExpenseModalForm
    sucess_message = "Success: Expense updated"
    success_url = reverse_lazy('expense')


class GuestCreateModal(BSModalCreateView):
    model = Guest
    model_type = 'guest'
    template_name = 'components/modals/create.html'
    form_class = GuestModalForm
    success_message = 'Success: Guest created.'
    success_url = reverse_lazy('guest')

    def test_func(self):
        return self.request.user.is_staff


class GuestDeleteModal(BSModalDeleteView):
    model = Guest
    context_object_name = 'guest'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Guest deleted'
    success_url = reverse_lazy('guest')

    def test_func(self):
        return self.request.user.is_staff


class GuestUpdateModal(BSModalUpdateView):
    model = Guest
    template_name = 'components/modals/update.html'
    form_class = GuestModalForm
    sucess_message = "Success: Guest updated"
    success_url = reverse_lazy('guest')


class RequestDeleteModal(BSModalDeleteView):
    model = Request
    context_object_name = 'trequest'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Request deleted'
    success_url = reverse_lazy('request')

    def test_func(self):
        return self.request.user.is_staff


class RequestUpdateModal(BSModalUpdateView):
    model = Request
    template_name = 'components/modals/update.html'
    form_class = RequestModalForm
    sucess_message = "Success: Request updated"
    success_url = reverse_lazy('request')


class NotifDeleteModal(BSModalDeleteView):
    model = Message
    context_object_name = 'notif'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Notif deleted'
    success_url = reverse_lazy('notif')
    # def test_func(self):
    #     return self.notif.user.is_superuser


class NotifUpdateModal(BSModalUpdateView):
    model = Message
    template_name = 'components/modals/update.html'
    form_class = NotifModalForm
    sucess_message = "Success: Notif updated"
    success_url = reverse_lazy('notif')


class NotifCreateModal(BSModalCreateView):
    model = Message
    model_type = 'notif'
    template_name = 'components/modals/create.html'
    form_class = NotifCreateModalForm
    success_message = 'Success: Notif created.'
    success_url = reverse_lazy('notif')

    def test_func(self):
        return self.request.user.is_staff


class BookingReadModal(BSModalReadView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        fee_objects = kwargs['object'].add_ons.all()
        if kwargs['object'].approved:
            status = "Approved"
        else:
            status = "No action"
        total = 0
        rate = int(kwargs['object'].room_id.rate)
        total += rate
        for fee_object in fee_objects:
            total += int(fee_object.amount)
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'booking'
        context['booking'] = kwargs['object']
        context['user'] = kwargs['object'].user_id
        context['room'] = f"Floor-{kwargs['object'].room_id.floor} Number-{kwargs['object'].room_id.number}"
        context['type'] = kwargs['object'].room_id.get_room_type_display()
        context['rate'] = rate
        context['fees'] = kwargs['object'].add_ons.all()
        context['total'] = total
        context['status'] = status
        return context

    def test_func(self):
        return self.request.user.is_staff


class BookingDeleteModal(BSModalDeleteView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Booking deleted'
    success_url = reverse_lazy('booking')

    def test_func(self):
        return self.notif.user.is_staff


class BookingUpdateModal(BSModalUpdateView):
    model = Booking
    template_name = 'components/modals/update.html'
    form_class = BookingModalForm
    sucess_message = "Success: Booking updated"
    success_url = reverse_lazy('booking')


class PropertyCreateModal(BSModalCreateView):
    model = Property
    model_type = 'property'
    template_name = 'components/modals/create.html'
    form_class = PropertyModalForm
    success_message = 'Success: Property created.'
    success_url = reverse_lazy('property')

    def test_func(self):
        return self.request.user.is_staff


class PropertyDeleteModal(BSModalDeleteView):
    model = Property
    context_object_name = 'propertyo'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Property deleted'
    success_url = reverse_lazy('property')
    # def test_func(self):
    #     return self.notif.user.is_superuser


class PropertyUpdateModal(BSModalUpdateView):
    model = Property
    template_name = 'components/modals/update.html'
    form_class = PropertyModalForm
    sucess_message = "Success: Property updated"
    success_url = reverse_lazy('property')


class RoomCreateModal(BSModalCreateView):
    model = Room
    model_type = 'room'
    template_name = 'components/modals/create.html'
    form_class = RoomModalForm
    success_message = 'Success: Room created.'
    success_url = reverse_lazy('room')

    def test_func(self):
        return self.request.user.is_staff


class RoomDeleteModal(BSModalDeleteView):
    model = Room
    context_object_name = 'room'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Room deleted'
    success_url = reverse_lazy('room')
    # def test_func(self):
    #     return self.notif.user.is_superuser


class RoomUpdateModal(BSModalUpdateView):
    model = Room
    template_name = 'components/modals/update.html'
    form_class = RoomModalForm
    sucess_message = "Success: Room updated"
    success_url = reverse_lazy('room')


class AdminAccReadModal(BSModalReadView):
    model = OwnerAccount
    context_object_name = 'adminacc'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'adminacc'
        context['adminacc'] = kwargs['object']
        context['birthday'] = kwargs['object'].birthday.strftime("%B %d, %Y")
        context['name'] = f"{kwargs['object'].user_id.first_name} {kwargs['object'].user_id.last_name}"
        context['type'] = kwargs['object'].get_user_type_display()

        return context

    def test_func(self):
        return self.request.user.is_staff


class AdminAccDeleteModal(BSModalDeleteView):
    model = OwnerAccount
    context_object_name = 'adminacc'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Admin Account deleted'
    success_url = reverse_lazy('admin_management')
    # def test_func(self):
    #     return self.notif.user.is_superuser


class AdminAccUpdateModal(BSModalUpdateView):
    model = OwnerAccount
    template_name = 'components/modals/update.html'
    form_class = AdminAccModalForm
    sucess_message = "Success: Admin Account updated"
    success_url = reverse_lazy('admin_management')

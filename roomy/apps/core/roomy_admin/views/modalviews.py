from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
# get_object_or_404, redirect, reverse
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout

from django.views import generic
from django.contrib import messages
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from apps.core.roomy_core.models import *
from apps.core.roomy_admin.modalforms import *


# LoginRequiredMixin, UserPassesTestMixin,
class BillingReadModal(LoginRequiredMixin, UserPassesTestMixin, BSModalReadView):
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


class BillingDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Billing
    context_object_name = 'billing'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Billing deleted'
    success_url = reverse_lazy('billing')

    def test_func(self):
        return self.request.user.is_staff


class BillingUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Billing
    template_name = 'components/modals/update.html'
    form_class = BillingModalForm
    sucess_message = "Success: Billing updated"
    success_url = reverse_lazy('billing')

    def test_func(self):
        return self.request.user.is_staff


class FeeDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Fee
    context_object_name = 'fee'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Fee deleted'
    success_url = reverse_lazy('fee')

    def test_func(self):
        return self.request.user.is_staff


class FeeUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Fee
    template_name = 'components/modals/update.html'
    form_class = FeeModalForm
    sucess_message = "Success: Fee updated"
    success_url = reverse_lazy('fee')

    def test_func(self):
        return self.request.user.is_staff


def FeeCreateModal(request, pk):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        data = {
            'property_id': Property.objects.get(pk=pk)
        }
        form = FeeModelForm(request.POST or None, initial=data)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
            return redirect('fee')
        else:
            context = {
                'form': form,
            }
            return render(request, "components/modals/create.html", context)
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)


def ManageTenantsModal(request, pk):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'viewtype': 'manage_tenants',
            'transaction': Transaction.objects.get(pk=pk),
            'tenants': TenantAccount.objects.filter(transaction_id__pk=pk),
        }
        return render(request, "components/modals/read.html", context)
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)


def RemoveTenantModal(request, pk, idk):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        if request.method == 'GET':
            context = {
                'viewtype': 'manage_tenants',
                'transaction': Transaction.objects.get(pk=pk),
                'tenant': TenantAccount.objects.get(pk=idk),
            }
            return render(request, "components/modals/delete.html", context)
        elif request.method == 'POST':
            tenant = TenantAccount.objects.get(pk=idk)
            tenant.transaction_id = None
            tenant.save()

            tenants = TenantAccount.objects.filter(transaction_id__pk=pk)
            if not tenants:
                transaction = Transaction.objects.get(pk=pk)
                transaction.active = False
                print(transaction)
                transaction.save()

            return HttpResponseRedirect(reverse('rental'))
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)


class RentalReadModal(LoginRequiredMixin, UserPassesTestMixin, BSModalReadView):
    model = Transaction
    context_object_name = 'transaction'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        fee_objects = kwargs['object'].add_ons.all()
        # fees = int(kwargs['object'].room_id.catalog_id.rate)
        fees = 0
        for fee_object in fee_objects:
            fees += int(fee_object.amount)
        if kwargs['object'].rated:
            rating = str(kwargs['object'].rating) + \
                kwargs['object'].rating_description
        else:
            rating = 'Unrated'
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'transaction'
        context['transaction'] = kwargs['object']
        context['date'] = Booking.objects.get(
            tenant_id__transaction_id=kwargs['object']).start_date.strftime("%Y, %B %d")
        context['room'] = f"Floor-{kwargs['object'].room_id.catalog_id.floor} Number-{kwargs['object'].room_id.number}"
        context['tenants'] = TenantAccount.objects.filter(
            transaction_id=kwargs['object'])
        context['add_ons'] = kwargs['object'].add_ons.all()
        context['total'] = fees
        context['rate'] = int(kwargs['object'].room_id.catalog_id.rate)
        context['rating'] = rating

        return context

    def test_func(self):
        return self.request.user.is_staff


class RentalDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Transaction
    context_object_name = 'transaction'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Transaction deleted'
    success_url = reverse_lazy('rental')

    def test_func(self):
        return self.request.user.is_staff


class RentalUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Transaction
    template_name = 'components/modals/update.html'
    form_class = TransactionModalForm
    sucess_message = "Success: Transaction updated"
    success_url = reverse_lazy('rental')

    def test_func(self):
        return self.request.user.is_staff


def AddTenantModal(request, pk):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        if request.method == 'GET':
            property_obj = Property.objects.get(pk=pk)
            rooms = []
            transactions = Transaction.objects.filter(
                room_id__catalog_id__property_id=property_obj)
            for transaction in transactions:
                rooms.append(transaction.room_id)
            context = {
                'viewtype': 'add_tenant',
                'property': property_obj,
                # 'rooms': Room.objects.filter(catalog_id__property_id=property_obj),
                'rooms': rooms,
            }
            return render(request, "components/modals/create.html", context)
        elif request.method == 'POST':
            print('POST')
            user_id = authenticate(
                username=request.POST['username'], password=request.POST['password'])
            transaction_id = Transaction.objects.get(
                room_id=request.POST.get('room'))

            try:
                print('get tenant')
                new_tenant = TenantAccount.objects.get(
                    user_id=user_id, transaction_id=transaction_id)
            except TenantAccount.DoesNotExist:
                print('new tenant')
                if user_id and transaction_id:
                    new_tenant = TenantAccount(
                        user_id=user_id, transaction_id=transaction_id)
                    new_tenant.save()
            room = transaction_id.room_id
            room.status = 1
            room.save()

            return HttpResponseRedirect(reverse('tenant'))
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)


class TenantReadModal(LoginRequiredMixin, UserPassesTestMixin, BSModalReadView):
    model = TenantAccount
    context_object_name = 'tenants'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        try:
            bday = kwargs['object'].birthday.strftime("%B %d, %Y")
        except:
            bday = "None"
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'tenants'
        context['tenant'] = kwargs['object']
        context['transaction'] = kwargs['object'].transaction_id
        context['birthday'] = bday

        return context

    def test_func(self):
        return self.request.user.is_staff


def ExpenseCreateModal(request, pk):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        data = {
            'property_id': Property.objects.get(pk=pk)
        }
        form = ExpenseModelForm(request.POST or None, initial=data)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
            return redirect('expense')
        else:
            context = {
                'form': form,
            }
            return render(request, "components/modals/create.html", context)
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)


class ExpenseDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Expense deleted'
    success_url = reverse_lazy('expense')

    def test_func(self):
        return self.request.user.is_staff


class ExpenseUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Expense
    template_name = 'components/modals/update.html'
    form_class = ExpenseModalForm
    sucess_message = "Success: Expense updated"
    success_url = reverse_lazy('expense')

    def test_func(self):
        return self.request.user.is_staff


class GuestCreateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalCreateView):
    model = Guest
    model_type = 'guest'
    template_name = 'components/modals/create.html'
    form_class = GuestModalForm
    success_message = 'Success: Guest created.'
    success_url = reverse_lazy('guest')

    def test_func(self):
        return self.request.user.is_staff


class GuestDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Guest
    context_object_name = 'guest'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Guest deleted'
    success_url = reverse_lazy('guest')

    def test_func(self):
        return self.request.user.is_staff


class GuestUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Guest
    template_name = 'components/modals/update.html'
    form_class = GuestModalForm
    sucess_message = "Success: Guest updated"
    success_url = reverse_lazy('guest')

    def test_func(self):
        return self.request.user.is_staff


class RequestDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Request
    context_object_name = 'trequest'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Request deleted'
    success_url = reverse_lazy('request')

    def test_func(self):
        return self.request.user.is_staff


class RequestUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Request
    template_name = 'components/modals/update.html'
    form_class = RequestUpdateModalForm
    sucess_message = "Success: Request updated"
    success_url = reverse_lazy('request')

    def test_func(self):
        return self.request.user.is_staff


class NotifDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Message
    context_object_name = 'notif'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Notif deleted'
    success_url = reverse_lazy('notif')

    def test_func(self):
        return self.request.user.is_staff


class NotifUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Message
    template_name = 'components/modals/update.html'
    form_class = NotifModalForm
    sucess_message = "Success: Notif updated"
    success_url = reverse_lazy('notif')

    def test_func(self):
        return self.request.user.is_staff


class NotifCreateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalCreateView):
    model = Message
    model_type = 'notif'
    template_name = 'components/modals/create.html'
    form_class = NotifCreateModalForm
    success_message = 'Success: Notif created.'
    success_url = reverse_lazy('notif')

    def test_func(self):
        return self.request.user.is_staff


class BookingReadModal(LoginRequiredMixin, UserPassesTestMixin, BSModalReadView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        fee_objects = kwargs['object'].add_ons.all()
        total = 0
        rate = int(kwargs['object'].catalog_id.rate)
        total += rate
        for fee_object in fee_objects:
            total += int(fee_object.amount)
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'booking'
        context['booking'] = kwargs['object']
        context['user'] = kwargs['object'].user_id
        context['room'] = f"Floor-{kwargs['object'].catalog_id.floor} "
        context['type'] = kwargs['object'].catalog_id.get_room_type_display()
        context['rate'] = rate
        context['fees'] = kwargs['object'].add_ons.all()
        context['total'] = total
        context['status'] = kwargs['object'].get_status_display()
        return context

    def test_func(self):
        return self.request.user.is_staff


class BookingDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Booking deleted'
    success_url = reverse_lazy('booking')

    def test_func(self):
        return self.request.user.is_staff


class BookingUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Booking
    template_name = 'components/modals/update.html'
    form_class = BookingModalForm
    sucess_message = "Success: Booking updated"
    success_url = reverse_lazy('booking')

    def test_func(self):
        return self.request.user.is_staff


class PropertyReadModal(LoginRequiredMixin, UserPassesTestMixin, BSModalReadView):
    model = Property
    context_object_name = 'property'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'property'
        context['property'] = kwargs['object']
        context['type'] = kwargs['object'].get_property_type_display()
        context['images'] = kwargs['object'].property_image.all()
        return context

    def test_func(self):
        return self.request.user.is_staff


def PropertyCreateModal(request):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        data = {
            'owner_id': OwnerAccount.objects.get(user_id=request.user)
        }
        form = PropertyModelForm(request.POST or None, initial=data)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('property_management'))
        else:
            context = {
                'form': form,
            }
            return render(request, "components/modals/create.html", context)
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)


class PropertyDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Property
    context_object_name = 'propertyo'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Property deleted'
    success_url = reverse_lazy('property_management')

    def test_func(self):
        return self.request.user.is_staff


class PropertyUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Property
    template_name = 'components/modals/update.html'
    form_class = PropertyModalForm
    sucess_message = "Success: Property updated"
    success_url = reverse_lazy('property_management')

    def test_func(self):
        return self.request.user.is_staff


class CatalogReadModal(LoginRequiredMixin, UserPassesTestMixin, BSModalReadView):
    model = RoomCatalog
    context_object_name = 'catalog'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'catalog'
        context['catalog'] = kwargs['object']
        context['type'] = kwargs['object'].get_room_type_display()
        context['images_3d'] = kwargs['object'].img_3d.all()
        context['images_2d'] = kwargs['object'].img_2d.all()
        return context

    def test_func(self):
        return self.request.user.is_staff


def CatalogCreateModal(request, pk):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        data = {
            'property_id': Property.objects.get(pk=pk)
        }
        form = CatalogModelForm(request.POST or None, initial=data)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('catalog_management'))
        else:
            context = {
                'form': form,
            }
            return render(request, "components/modals/create.html", context)
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)


class CatalogDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = RoomCatalog
    context_object_name = 'catalog'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Catalog deleted'
    success_url = reverse_lazy('catalog_management')

    def test_func(self):
        return self.request.user.is_staff


class CatalogUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = RoomCatalog
    template_name = 'components/modals/update.html'
    form_class = RoomCatalogModalForm
    sucess_message = "Success: Catalog updated"
    success_url = reverse_lazy('catalog_management')

    def test_func(self):
        return self.request.user.is_staff


class RoomReadModal(LoginRequiredMixin, UserPassesTestMixin, BSModalReadView):
    model = Room
    context_object_name = 'room'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'room'
        context['room'] = kwargs['object']
        # context['type'] = kwargs['object'].get_room_type_display()
        # context['images_3d'] = kwargs['object'].image_3d.all()
        # context['images_2d'] = kwargs['object'].image_2d.all()
        return context

    def test_func(self):
        return self.request.user.is_staff


# class RoomCreateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalCreateView):
#     model = Room
#     model_type = 'room'
#     template_name = 'components/modals/create.html'
#     form_class = RoomModalForm
#     success_message = 'Success: Room created.'
#     success_url = reverse_lazy('room_management')

#     def test_func(self):
#         return self.request.user.is_staff

def RoomCreateModal(request, pk):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        data = {
            'catalog_id': RoomCatalog.objects.get(pk=pk)
        }
        form = RoomModelForm(request.POST or None, initial=data)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('room_management'))
        else:
            context = {
                'form': form,
            }
            return render(request, "components/modals/create.html", context)
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)


class RoomDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = Room
    context_object_name = 'room'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Room deleted'
    success_url = reverse_lazy('room_management')

    def test_func(self):
        return self.request.user.is_staff


class RoomUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = Room
    template_name = 'components/modals/update.html'
    form_class = RoomModalForm
    sucess_message = "Success: Room updated"
    success_url = reverse_lazy('room_management')

    def test_func(self):
        return self.request.user.is_staff


class OnotifUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = OwnerNotification
    template_name = 'components/modals/update.html'
    form_class = OnotifModalForm
    sucess_message = "Success: Owner Notif updated"
    success_url = reverse_lazy('owner_notification')

    def test_func(self):
        return self.request.user.is_staff


class OnotifReadModal(LoginRequiredMixin, UserPassesTestMixin, BSModalReadView):
    model = OwnerNotification
    context_object_name = 'onotif'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'onotif'
        context['onotif'] = kwargs['object']
        return context

    def test_func(self):
        return self.request.user.is_staff


class AdminAccReadModal(LoginRequiredMixin, UserPassesTestMixin, BSModalReadView):
    model = OwnerAccount
    context_object_name = 'adminacc'
    template_name = 'components/modals/read.html'

    def get_context_data(self, **kwargs):
        try:
            bday = kwargs['object'].birthday.strftime("%B %d, %Y")
        except e:
            bday = "None"
        context = super().get_context_data(**kwargs)
        context['viewtype'] = 'adminacc'
        context['adminacc'] = kwargs['object']
        context['birthday'] = bday
        context['name'] = f"{kwargs['object'].user_id.first_name} {kwargs['object'].user_id.last_name}"
        context['type'] = kwargs['object'].get_user_type_display()

        return context

    def test_func(self):
        return self.request.user.is_staff


class AdminAccDeleteModal(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    model = OwnerAccount
    context_object_name = 'adminacc'
    template_name = 'components/modals/delete.html'
    success_message = 'Success: Admin Account deleted'
    success_url = reverse_lazy('admin_management')

    def test_func(self):
        return self.request.user.is_staff


class AdminAccUpdateModal(LoginRequiredMixin, UserPassesTestMixin, BSModalUpdateView):
    model = OwnerAccount
    template_name = 'components/modals/update.html'
    form_class = AdminAccModalForm
    sucess_message = "Success: Admin Account updated"
    success_url = reverse_lazy('admin_management')

    def test_func(self):
        return self.request.user.is_staff

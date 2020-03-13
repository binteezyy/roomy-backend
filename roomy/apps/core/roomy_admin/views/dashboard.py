from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse  # get_object_or_404

from apps.core.roomy_admin.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver
from datetime import datetime, date

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from apps.core.roomy_core.models import *

context = {
    "title": "Roomy",
}

# home


def home(request):

    next = request.GET.get('next')

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        properties = Property.objects.filter(owner_id__user_id=request.user)
        transactions = Transaction.objects.filter(
            room_id__catalog_id__property_id__owner_id__user_id=request.user)

        month_years = []
        for transaction in transactions:
            month_years.append(transaction.billing_date)

        context = {
            'properties': properties,
            'month_years': month_years,
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/home.html", context)
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

# home ajax


def home_ajax(request):
    val = request.GET.get('val', None)
    # my = request.GET.get('my', None)
    print(val)
    # month, year = my.split('-')
    # print(month)
    # print(year)
    property_o = Property.objects.get(owner_id__user_id=request.user, pk=val)
    active_tenants = TenantAccount.objects.filter(
        transaction_id__active=True, transaction_id__room_id__catalog_id__property_id=property_o).count()
    pending_bookings = Booking.objects.filter(
        status=0, catalog_id__property_id__owner_id__user_id=request.user, catalog_id__property_id=property_o).count()
    active_rooms = Room.objects.filter(
        catalog_id__property_id=property_o).exclude(status=0).count()
    avail_rooms = Room.objects.filter(
        catalog_id__property_id=property_o, status=0).count()
    billings = Billing.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o,
                                      paid=True, time_stamp__month__gte=date.today().month, time_stamp__year__gte=date.today().year)
    payments = 0

    for billing in billings:
        for fee in billing.billing_fee.all():
            payments += int(fee.amount)

    expenses_o = Expense.objects.filter(property_id=property_o, time_stamp__month__gte=date.today(
    ).month, time_stamp__year__gte=date.today().year)
    expenses = 0
    for expense in expenses_o:
        expenses += int(expense.amount)

    net_income = payments - expenses

    data = {
        'active_tenants': active_tenants,
        'pending_bookings': pending_bookings,
        'active_rooms': active_rooms,
        'avail_rooms': avail_rooms,
        'payments': payments,
        'expenses': expenses,
        'net_income': net_income,
    }
    return JsonResponse(data)

# rental


@login_required
@user_passes_test(lambda u: u.is_staff)
def rental(request):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/rental.html", context)
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


# transaction signals
@receiver(m2m_changed, sender=Transaction.add_ons.through)
def create_billing_on_transaction_save(sender, instance, **kwargs):
    print('start')
    action = kwargs.pop('action', None)
    if action == "post_add":
        print('transaction created')
        try:
            billing = Billing.objects.get(
                time_stamp=instance.billing_date, transaction_id__pk=instance.pk)
            billing.billing_fee.set(instance.add_ons.all())
            print('billing exists')
        except Billing.DoesNotExist:
            billing = Billing(time_stamp=instance.billing_date,
                              transaction_id=instance)
            billing.save()
            print(instance.add_ons.all())
            billing.billing_fee.set(instance.add_ons.all())
            print('does not exists')
        print(billing)
# tenant


@login_required
@user_passes_test(lambda u: u.is_staff)
def tenant(request):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/tenant.html", context)
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


# guest


@login_required
@user_passes_test(lambda u: u.is_staff)
def guest(request):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/guest.html", context)
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

# request


@login_required
@user_passes_test(lambda u: u.is_staff)
def tenant_request(request):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/request.html", context)
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

# notifications


@login_required
@user_passes_test(lambda u: u.is_staff)
def notif(request):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/notifs.html", context)
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

# booking


@login_required
@user_passes_test(lambda u: u.is_staff)
def booking(request):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/booking.html", context)
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


# booking signals


@receiver(pre_save, sender=Booking)
def error_save_when_no_rooms_avail(sender, instance, *args, **kwargs):
    avail_rooms = Room.objects.filter(catalog_id=instance.catalog_id, status=0)
    if not avail_rooms and instance.status == 0:
        raise ValidationError('No rooms available for catalog')


@receiver(post_save, sender=Booking)
def create_notif_on_status_change(sender, instance, created, **kwargs):
    print("Create notif")
    if instance.status == 1:
        tenant_notif = Message(tenant_id=instance.tenant_id, title="Approved!",
                               body=f'Your booking for {instance.catalog_id.name} has been approved! Please visit your application for details')
        tenant_notif.save()
        print(tenant_notif)
    elif instance.status == 2:
        tenant_notif = Message(tenant_id=instance.tenant_id, title="Denied",
                               body=f'Your booking for {instance.catalog_id.name} has been denied. Please try and explore other catalogs and retry your booking.')
        tenant_notif.save()
        print(tenant_notif)
    elif instance.status == 3:
        tenant_notif = Message(tenant_id=instance.tenant_id, title="Cancelled",
                               body=f'You have cancelled your booking for {instance.catalog_id.name}. Please try and explore other catalogs and retry your booking.')
        tenant_notif.save()
        print(tenant_notif)
    # print("send notif to channel")
    # channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.group_send)(
    #     instance.tenant_id.user_id.id, {"type": "user_message",
    #                                     "event": "New booking notification",
    #                                     "message": f'New booking notification for {instance.catalog_id.name}'
    #                                     })


@receiver(post_save, sender=Request)
def create_notif_on_status_change_request(sender, instance, created, **kwargs):
    print("Create notif")
    if instance.status == 1:
        tenant_notif = Message(tenant_id=TenantAccount.objects.get(transaction_id=instance.transaction_id), title="Approved!",
                               body=f'Your request for {instance.subject} has been approved and is currently under process.')
        tenant_notif.save()
        print(tenant_notif)
    if instance.status == 2:
        tenant_notif = Message(tenant_id=TenantAccount.objects.get(transaction_id=instance.transaction_id), title="Denied",
                               body=f'Your request for {instance.subject} has been denied. Please try and create another request if needed.')
        tenant_notif.save()
        print(tenant_notif)

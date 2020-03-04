from django.http import HttpResponse
from django.shortcuts import render  # get_object_or_404, redirect, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from apps.core.roomy_core.models import *
from django.contrib.auth import authenticate, login, logout

import json
from pprint import pprint

# @login_required
# @user_passes_test(lambda u: u.is_staff)


@login_required
@user_passes_test(lambda u: u.is_staff)
def billing_table(request, pk):
    billings = Billing.objects.filter(
        transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, transaction_id__room_id__catalog_id__property_id__pk=pk)

    data = []
    for billing in billings:
        if billing.paid == True:
            paid = "Paid"
        else:
            paid = "Not paid"

        time = billing.time_stamp.strftime("%Y, %B %d")
        fees = ' | '.join([str(i) for i in billing.billing_fee.all()])
        room = f'Property: {billing.transaction_id.room_id.catalog_id.property_id.name} \n Room: Floor-{billing.transaction_id.room_id.catalog_id.floor} Number-{billing.transaction_id.room_id.number}'

        x = {"fields": {"id": billing.pk,
                        "time": time,
                        "room": room,
                        "fee": fees,
                        "paid": paid,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_staff)
def fee_table(request, pk):
    fees = Fee.objects.filter(property_id__owner_id__user_id=request.user, property_id__pk=pk).exclude(fee_type=2)

    data = []
    for fee in fees:
        x = {"fields": {"id": fee.pk,
                        "type": fee.get_fee_type_display(),
                        "description": fee.description,
                        "amount": str(fee.amount),
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_staff)
def rental_table(request,pk):
    transactions = Transaction.objects.filter(
        active=True, room_id__catalog_id__property_id__owner_id__user_id=request.user, room_id__catalog_id__property_id__pk=pk)

    data = []
    for transaction in transactions:
        room = f'Room: Floor-{transaction.room_id.catalog_id.floor} Number-{transaction.room_id.number}'
        date = Transaction.objects.get(pk=transaction.pk).billing_date.strftime("%Y, %B %d")
        x = {"fields": {"id": transaction.pk,
                        "room": room,
                        "date": date,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_staff)
def tenant_table(request, pk):
    tenants = TenantAccount.objects.filter(
        transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, transaction_id__room_id__catalog_id__property_id__pk=pk)

    data = []
    for tenant in tenants:
        if tenant.transaction_id.active:
            room = f'Room: Floor-{tenant.transaction_id.room_id.catalog_id.floor} Number-{tenant.transaction_id.room_id.number}'
        else:
            room = "Inacitve"
        x = {"fields": {"id": tenant.pk,
                        "name": f'{tenant.user_id.username} - {tenant.user_id.first_name} {tenant.user_id.last_name}',
                        "room": room,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_staff)
def expense_table(request, pk):
    expenses = Expense.objects.filter(
        property_id__owner_id__user_id=request.user, property_id__pk=pk)

    data = []
    for expense in expenses:
        time = expense.time_stamp.strftime("%Y, %B %d")
        x = {"fields": {"id": expense.pk,
                        "time": time,
                        "description": expense.description,
                        "amount": str(expense.amount),
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_staff)
def guest_table(request, pk):
    guests = Guest.objects.filter(
        transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, transaction_id__room_id__catalog_id__property_id__pk=pk)

    data = []
    for guest in guests:
        date = guest.time_stamp.strftime("%Y, %B %d")
        if guest.inside:
            status = "In"
        else:
            status = "Out"
        x = {"fields": {"id": guest.pk,
                        "name": guest.name,
                        "date": date,
                        "room": f'Room: Floor-{guest.transaction_id.room_id.catalog_id.floor} Number-{guest.transaction_id.room_id.number}',
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_staff)
def request_table(request, pk):
    tenant_requests = Request.objects.filter(
        transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, transaction_id__room_id__catalog_id__property_id__pk=pk)

    data = []
    for tenant_request in tenant_requests:
        date = tenant_request.time_stamp.strftime("%Y, %B %d")
        if tenant_request.status:
            status = "Done"
        else:
            status = "Not Done"
        x = {"fields": {"id": tenant_request.pk,
                        "subject": tenant_request.subject,
                        "description": tenant_request.description,
                        "date": date,
                        "room": f'Room: Floor-{tenant_request.transaction_id.room_id.catalog_id.floor} Number-{tenant_request.transaction_id.room_id.number}',
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_staff)
def notif_table(request):
    notifs = Message.objects.filter(
        tenant_id__transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user)

    data = []
    for notif in notifs:
        date = notif.time_stamp.strftime("%Y, %B %d")
        if notif.sent:
            status = "Sent"
        else:
            status = "Not Sent"
        x = {"fields": {"id": notif.pk,
                        "tenant": f'{notif.tenant_id.user_id.username} - {notif.tenant_id.user_id.first_name} {notif.tenant_id.user_id.last_name}',
                        "title": notif.title,
                        "body": notif.body,
                        "date": date,
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_staff)
def booking_table(request, pk):
    bookings = Booking.objects.filter(status=0,
        catalog_id__property_id__owner_id__user_id=request.user, catalog_id__property_id__pk=pk)

    data = []
    for booking in bookings:
        x = {"fields": {"id": booking.pk,
                        "user": f'{booking.user_id.username} - {booking.user_id.first_name} {booking.user_id.last_name}',
                        "room": f'Room: Floor-{booking.catalog_id.floor}',
                        "status": booking.get_status_display(),
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_staff)
def property_table(request):
    propertys = Property.objects.filter(owner_id__user_id=request.user)

    data = []
    for property_obj in propertys:
        if property_obj.property_image.all():
            images = ' | '.join([str(i)
                                 for i in property_obj.property_image.all()])
        else:
            images = "Empty"
        x = {"fields": {"id": property_obj.pk,
                        "name": property_obj.name,
                        "type": property_obj.get_property_type_display(),
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')

@login_required
@user_passes_test(lambda u: u.is_staff)
def catalog_table(request, pk):
    catalogs = RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user, property_id__pk=pk)

    data = []
    for catalog in catalogs:
        if catalog.name:
            name = catalog.name
        else:
            name = "None"
        x = {"fields": {"id": catalog.pk,
                        "name": name,
                        "floor": catalog.floor,
                        "rate": int(catalog.rate),
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')

@login_required
@user_passes_test(lambda u: u.is_staff)
def room_table(request, pk):
    rooms = Room.objects.filter(catalog_id__property_id__owner_id__user_id=request.user, catalog_id__pk=pk)

    data = []
    for room in rooms:
        if room.status == 2:
            status = "Occupied"
        elif room.status == 1:
            status = "Shared"
        else:
            status = "Vacant"
        if room.catalog_id.img_2d.all():
            images2d = ' | '.join([str(i)
                                   for i in room.catalog_id.img_2d.all()])
        else:
            images2d = 'Empty'
        if room.catalog_id.img_3d.all():
            images3d = ' | '.join([str(i)
                                   for i in room.catalog_id.img_3d.all()])
        else:
            images3d = 'Empty'
        if room.catalog_id.name:
            name = room.catalog_id.name
        else:
            name = "None"
        x = {"fields": {"id": room.pk,
                        "catalog": room.catalog_id.name,
                        "number": f'Number-{room.number}',
                        "property": room.catalog_id.property_id.name,
                        "name": name,
                        "floorno": f'Room: Floor-{room.catalog_id.floor} Number-{room.number}',
                        "rate": int(room.catalog_id.rate),
                        "type": room.catalog_id.get_room_type_display(),
                        "images2d": images2d,
                        "images3d": images3d,
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')

@login_required
@user_passes_test(lambda u: u.is_staff)
def onotif_table(request):
    notifs = OwnerNotification.objects.filter(owner_id__user_id=request.user)

    data = []
    for notif in notifs:
        date = notif.time_stamp.strftime("%Y, %B %d")
        if notif.read:
            status = "Read"
        else:
            status = "Unread"
        x = {"fields": {"id": notif.pk,
                        "title": notif.title,
                        "body": notif.body,
                        "date": date,
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_acc_table(request):
    admin_accs = OwnerAccount.objects.all()

    data = []
    for admin_acc in admin_accs:
        # if admin_acc.property_id:
        #     property_name = admin_acc.property_id.name
        # else:
        #     property_name = 'None. Tenant/Guest'
        x = {"fields": {"id": admin_acc.pk,
                        "type": admin_acc.get_user_type_display(),
                        "name": f'{admin_acc.user_id.username} - {admin_acc.user_id.first_name} {admin_acc.user_id.last_name}',
                        "property": "property_name",
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')

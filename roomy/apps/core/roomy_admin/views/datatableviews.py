from django.http import HttpResponse
from django.shortcuts import render  # get_object_or_404, redirect, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from apps.core.roomy_core.models import *

import json
from pprint import pprint

# @login_required
# @user_passes_test(lambda u: u.is_superuser)


def billing_table(request):
    billings = Billing.objects.all()

    data = []
    for billing in billings:
        if billing.paid == True:
            paid = "Paid"
        else:
            paid = "Not paid"

        time = billing.time_stamp.strftime("%Y, %B %d")
        fees = ' | '.join([str(i) for i in billing.billing_fee.all()])
        room = f'Property: {billing.transaction_id.room_id.property_id.name} \n Room: Floor-{billing.transaction_id.room_id.floor} Number-{billing.transaction_id.room_id.number}'

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


def fee_table(request):
    fees = Fee.objects.all()

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


def rental_table(request):
    transactions = Transaction.objects.filter(active=True)

    data = []
    for transaction in transactions:
        room = f'Room: Floor-{transaction.room_id.floor} Number-{transaction.room_id.number}'
        date = transaction.start_date.strftime("%Y, %B %d")
        x = {"fields": {"id": transaction.pk,
                        "room": room,
                        "date": date,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


def tenant_table(request):
    tenants = UserAccount.objects.filter(user_type=1)

    data = []
    for tenant in tenants:
        x = {"fields": {"id": tenant.pk,
                        "name": f'{tenant.user_id.username} - {tenant.user_id.first_name} {tenant.user_id.last_name}',
                        "room": f'Room: Floor-{tenant.transaction_id.room_id.floor} Number-{tenant.transaction_id.room_id.number}',
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


def expense_table(request):
    expenses = Expense.objects.all()

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


def guest_table(request):
    guests = Guest.objects.all()

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
                        "room": f'Room: Floor-{guest.transaction_id.room_id.floor} Number-{guest.transaction_id.room_id.number}',
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


def request_table(request):
    tenant_requests = Request.objects.all()

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
                        "room": f'Room: Floor-{tenant_request.transaction_id.room_id.floor} Number-{tenant_request.transaction_id.room_id.number}',
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


def notif_table(request):
    notifs = Message.objects.all()

    data = []
    for notif in notifs:
        date = notif.time_stamp.strftime("%Y, %B %d")
        if notif.sent:
            status = "Sent"
        else:
            status = "Not Sent"
        x = {"fields": {"id": notif.pk,
                        "user": f'{notif.user_id.username} - {notif.user_id.first_name} {notif.user_id.last_name}',
                        "title": notif.title,
                        "body": notif.body,
                        "date": date,
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


def booking_table(request):
    bookings = Booking.objects.all()

    data = []
    for booking in bookings:
        if booking.approved:
            status = "Approved"
        else:
            status = "No Action Yet"
        x = {"fields": {"id": booking.pk,
                        "user": f'{booking.user_id.username} - {booking.user_id.first_name} {booking.user_id.last_name}',
                        "room": f'Room: Floor-{booking.room_id.floor} Number-{booking.room_id.number}',
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


def property_table(request):
    propertys = Property.objects.all()

    data = []
    for property_obj in propertys:
        if property_obj.property_image.all():
            images = ' | '.join([str(i)
                                 for i in property_obj.property_image.all()])
        else:
            images = "Empty"
        x = {"fields": {"id": property_obj.pk,
                        "name": property_obj.name,
                        "description": property_obj.description,
                        "images": images,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


def room_table(request):
    rooms = Room.objects.all()

    data = []
    for room in rooms:
        if UserAccount.objects.filter(transaction_id__room_id=room):
            status = "Occupied"
        else:
            status = "Vacant"
        if room.image_2d.all():
            images2d = ' | '.join([str(i)
                                   for i in room.image_2d.all()])
        else:
            images2d = 'Empty'
        if room.image_3d.all():
            images3d = ' | '.join([str(i)
                                   for i in room.image_3d.all()])
        else:
            images3d = 'Empty'
        x = {"fields": {"id": room.pk,
                        "property": room.property_id.name,
                        "floorno": f'Room: Floor-{room.floor} Number-{room.number}',
                        "rate": int(room.rate),
                        "type": room.get_room_type_display(),
                        "images2d": images2d,
                        "images3d": images3d,
                        "status": status,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')


def admin_acc_table(request):
    admin_accs = UserAccount.objects.all()

    data = []
    for admin_acc in admin_accs:
        if admin_acc.property_id:
            property_name = admin_acc.property_id.name
        else:
            property_name = 'None. Tenant/Guest'
        x = {"fields": {"id": admin_acc.pk,
                        "type": admin_acc.get_user_type_display(),
                        "name": f'{admin_acc.user_id.username} - {admin_acc.user_id.first_name} {admin_acc.user_id.last_name}',
                        "property": property_name,
                        }}
        data.append(x)
    data = json.dumps(data)
    pprint(data)
    return HttpResponse(data, content_type='application/json')

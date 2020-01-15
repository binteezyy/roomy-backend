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

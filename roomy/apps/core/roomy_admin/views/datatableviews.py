from django.http import HttpResponse
from django.shortcuts import render  # get_object_or_404, redirect, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from apps.core.roomy_core.models import *


# @login_required
# @user_passes_test(lambda u: u.is_superuser)
def billing_table(request):
    import json
    from pprint import pprint

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

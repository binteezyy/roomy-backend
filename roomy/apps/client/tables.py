from django.urls import path, include
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts                   import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators     import login_required
# MODELS
from django.db.models                   import Q
from apps.core.roomy_core.models import *
import json


app_name = 'tables'

@login_required
def RequestsTable(request,pk):
    requests = Request.objects.filter(transaction_id= Booking.objects.get(pk=pk).tenant_id.transaction_id.pk)
    data = []
    for r in requests:
        print(r)
        x = {"status": r.get_status_display(),
             "subject" :r.subject,
             "description": r.description,
             "date-created":"may lawit",
             }
        data.append(x)
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')


@login_required
def BillingsTable(request,pk):
    billings = Billing.objects.filter(transaction_id= Booking.objects.get(pk=pk).tenant_id.transaction_id.pk)
    data = []
    for r in billings:
        print(r)
        x = {"status": str(r.get_date()),
             "subject" : str(r.billing_total()),
             "date-created":"may lawit",
             }
        data.append(x)
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

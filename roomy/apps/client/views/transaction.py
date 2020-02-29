from django.shortcuts                               import render
from django.core.paginator                          import Paginator
from django.db.models                               import Q
from django.shortcuts                               import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators                 import login_required
from apps.core.roomy_core.models import *

context = {
    "TITLE": "",
    "viewtype": "transaction"
}


@login_required
def booking_modal(request,pk):
    return render(request,"web/components/property/modal/booking.html",context)

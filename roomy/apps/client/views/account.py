from django.shortcuts                               import render
from django.core.paginator                          import Paginator
from django.db.models                               import Q
from django.shortcuts                               import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators                 import login_required
from apps.core.roomy_core.models import *

context = {
    "TITLE": "My Account",
    "viewtype": "explore"
}

def bookings(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(
            Q(user_id=request.user)
        )
        transactions = TenantAccount.objects.filter(
            Q(user_id=request.user)
        )
        context.update({
            "account_view":"booking",
            "bookings": bookings,
        })
        return render(request,"web/components/account/components/booking/list.html",context)
    else:
        return redirect('login')

def BookingView(request,pk):
    acc = Booking.objects.get(pk=pk)
    if request.user.is_authenticated and request.user == acc.user_id:
        roomies = Transaction.objects.filter(pk = acc.tenant_id.transaction_id.pk)
        catalog = RoomCatalog.objects.get(pk = acc.tenant_id.transaction_id.room_id.catalog_id.pk)
        room = Room.objects.get(pk=acc.tenant_id.transaction_id.room_id.pk)
        context.update({
            "account_view":"booking",
            "tenant_account": acc,
            "roomies": roomies,
            "catalog": catalog,
            "room": room,
        })
        if request.user_agent.is_mobile:
            return render(request,"mobile-native/components/account/components/booking/view.html",context)
        else:
            return render(request,"web/components/account/components/booking/view.html",context)
    else:
        return redirect('login')

def saved(request):
    if request.user.is_authenticated:

        context.update({
            "account_view":"saved",
        })
        if request.user_agent.is_mobile:
            return render(request,"mobile-native/components/account/components/saved.html",context)
        else:
            return render(request,"web/components/account/components/saved.html",context)
    else:
        return redirect('login')

def messages(request):
    if request.user.is_authenticated:

        context.update({
            "account_view":"messages",
        })
        if request.user_agent.is_mobile:
            return render(request,"mobile-native/components/account/components/messages.html",context)
        else:
            return render(request,"web/components/account/components/messages.html",context)
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:

        context.update({
            "account_view":"messages",
        })
        if request.user_agent.is_mobile:
            return render(request,"mobile-native/components/account/components/profile.html",context)
        else:
            return render(request,"web/components/account/components/profile.html",context)
    else:
        return redirect('login')

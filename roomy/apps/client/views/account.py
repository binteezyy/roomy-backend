from django.shortcuts                               import render
from django.core.paginator                          import Paginator
from django.db.models                               import Q
from django.shortcuts                               import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators                 import login_required
from apps.core.roomy_core.models import *
from ..forms                                        import *
context = {
    "TITLE": "My Account",
    "viewtype": "explore"
}

@login_required(login_url='/login/')
def bookings(request):
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
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/account/components/booking/list.html",context)
    else:
        return render(request,"web/components/account/components/booking/list.html",context)


def BookingView(request,pk):
    acc = Booking.objects.get(pk=pk)
    if request.user.is_authenticated and request.user == acc.user_id:
        transactions = Transaction.objects.get(pk = acc.tenant_id.transaction_id.pk)
        catalog = RoomCatalog.objects.get(pk = acc.tenant_id.transaction_id.room_id.catalog_id.pk)
        room = Room.objects.get(pk=acc.tenant_id.transaction_id.room_id.pk)
        billings = Billing.objects.filter(transaction_id=transactions)[:3]
        try:
            requests = Request.objects.filter( Q(transaction_id=acc.tenant_id.transaction_id)).order_by('-time_stamp')[0]
        except Exception as e:
            requests = None
        context.update({
            "account_view":"booking",
            "tenant_account": acc,
            "roomies": transactions,
            "catalog": catalog,
            "room": room,
            "requests": requests,
            "booking": acc,
            "billings":billings,
        })

        if request.user_agent.device.family == "Roomy Native":
            return render(request,"mobile-native/components/account/components/booking/view.html",context)
        else:
            return render(request,"web/components/account/components/booking/view.html",context)
    else:
        return redirect('login')

def BookingRequest(request,pk):
    form = RoomRequestForm()
    transactions = Transaction.objects.get(pk =pk)

    context.update({
        "form":form
    })

    if request.method == "POST":
        for key, value in request.POST.items():
           print('Key: %s' % (key) )

        try:
            r = Request.objects.create(
                subject = "Room Request",
                description = request.POST
                .get('message'),
                transaction_id = transactions
            )
        except Exception as e:
            print(e)
        return redirect(request.META.get('HTTP_REFERER', 'index'))
    else:

        return render(request,"web/components/account/components/booking/request/base.html",context)

def BookingRequestList(request,pk):
    booking = Booking.objects.get(pk=pk)

    context.update({
        "booking": booking,
    })
    return render(request,"web/components/account/components/booking/request/list.html",context)

def BookingBillingList(request,pk):
    booking = Booking.objects.get(pk=pk)

    context.update({
        "booking": booking,
    })
    return render(request,"web/components/account/components/booking/billing/list.html",context)

def saved(request):
    if request.user.is_authenticated:

        context.update({
            "account_view":"saved",
        })
        if request.user_agent.device.family == "Roomy Native":
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
        if request.user_agent.device.family == "Roomy Native":
            return render(request,"mobile-native/components/account/components/messages.html",context)
        else:
            return render(request,"web/components/account/components/messages.html",context)
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:

        context.update({
            "account_view":"profile",
        })
        if request.user_agent.device.family == "Roomy Native":
            return render(request,"mobile-native/components/account/components/profile.html",context)
        else:
            return render(request,"web/components/account/components/profile.html",context)
    else:
        return redirect('login')

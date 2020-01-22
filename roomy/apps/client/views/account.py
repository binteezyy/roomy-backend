from django.shortcuts                               import render
from django.core.paginator                          import Paginator
from django.db.models                               import Q
from django.shortcuts                               import render, get_object_or_404, redirect, reverse
from apps.core.roomy_core.models import *

context = {
    "TITLE": "My Account",
    "viewtype": "explore"
}

def bookings(request):
    if request.user.is_authenticated:

        context.update({
            "account_view":"booking",
        })
        return render(request,"components/account/components/bookings.html",context)
    else:
        return redirect('login')

def saved(request):
    if request.user.is_authenticated:

        context.update({
            "account_view":"saved",
        })
        return render(request,"components/account/components/saved.html",context)
    else:
        return redirect('login')

def messages(request):
    if request.user.is_authenticated:

        context.update({
            "account_view":"messages",
        })
        return render(request,"components/account/components/messages.html",context)
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:

        context.update({
            "account_view":"profile",
        })
        return render(request,"components/account/components/profile.html",context)
    else:
        return redirect('login')
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse  # get_object_or_404

from apps.core.roomy_admin.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.core.roomy_core.models import *

context = {
    "title": "Roomy",
}

#home
@login_required
@user_passes_test(lambda u: u.is_staff)
def home(request):

    return render(request, "components/dashboard/home.html", context)

# rental
@login_required
@user_passes_test(lambda u: u.is_staff)
def rental(request):

    return render(request, "components/dashboard/rental.html", context)

# tenant
@login_required
@user_passes_test(lambda u: u.is_staff)
def tenant(request):

    return render(request, "components/dashboard/tenant.html", context)

# billing
@login_required
@user_passes_test(lambda u: u.is_staff)
def billing(request):

    return render(request, "components/dashboard/billing.html", context)

#guest
@login_required
@user_passes_test(lambda u: u.is_staff)
def guest(request):
    return render(request, "components/dashboard/guest.html", context)

#request
@login_required
@user_passes_test(lambda u: u.is_staff)
def tenant_request(request):

    return render(request, "components/dashboard/request.html", context)

#notifications
@login_required
@user_passes_test(lambda u: u.is_staff)
def notif(request):

    return render(request, "components/dashboard/notifs.html", context)

#booking
@login_required
@user_passes_test(lambda u: u.is_staff)
def booking(request):

    return render(request, "components/dashboard/booking.html", context)

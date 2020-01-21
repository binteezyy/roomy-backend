from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse  # get_object_or_404

from apps.core.roomy_admin.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.core.roomy_core.models import *

context = {
    "title": "Roomy",
}

# billing
@login_required
@user_passes_test(lambda u: u.is_staff)
def billing(request):

    return render(request, "components/cashflow/billing.html", context)

#expense
@login_required
@user_passes_test(lambda u: u.is_staff)
def expense(request):

    return render(request, "components/cashflow/expense.html", context)

#fee
@login_required
@user_passes_test(lambda u: u.is_staff)
def fee(request):

    return render(request, "components/cashflow/fee.html", context)

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse  # get_object_or_404

from apps.core.roomy_admin.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.core.roomy_core.models import *

context = {
    "title": "Roomy",
}

#property management
@login_required
@user_passes_test(lambda u: u.is_staff)
def property_management(request):

    return render(request, "components/management/property_management.html", context)

#room management
@login_required
@user_passes_test(lambda u: u.is_staff)
def room_management(request):

    return render(request, "components/management/room_management.html", context)

#admin management
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_management(request):

    return render(request, "components/management/admin_management.html", context)

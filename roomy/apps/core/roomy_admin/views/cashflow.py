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

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user)
        }
        return render(request, "components/cashflow/billing.html", context)
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)

# expense


@login_required
@user_passes_test(lambda u: u.is_staff)
def expense(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user)
        }
        return render(request, "components/cashflow/expense.html", context)
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)

# fee


@login_required
@user_passes_test(lambda u: u.is_staff)
def fee(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user)
        }
        return render(request, "components/cashflow/fee.html", context)
    else:
        logout(request)
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('admin-index'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)

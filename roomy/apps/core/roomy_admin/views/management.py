from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse  # get_object_or_404

from apps.core.roomy_admin.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.core.roomy_core.models import *

context = {
    "title": "Roomy",
}

# property management


@login_required
@user_passes_test(lambda u: u.is_staff)
def property_management(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/management/property_management.html", context)
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

# catalog management


@login_required
@user_passes_test(lambda u: u.is_staff)
def catalog_management(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/management/catalog_management.html", context)
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
# room management


@login_required
@user_passes_test(lambda u: u.is_staff)
def room_management(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/management/room_management.html", context)
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

# owner notification
@login_required
@user_passes_test(lambda u: u.is_staff)
def owner_notification(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/management/owner_notification.html", context)
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
    
# admin management


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_management(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        return render(request, "components/management/account_management.html")
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

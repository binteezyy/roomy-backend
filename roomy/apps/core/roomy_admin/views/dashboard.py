from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse  # get_object_or_404

from apps.core.roomy_admin.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.core.roomy_core.models import *

context = {
    "title": "Roomy",
}

# home


def home(request):

    next = request.GET.get('next')

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/home.html", context)
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

# rental


@login_required
@user_passes_test(lambda u: u.is_staff)
def rental(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/rental.html", context)
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

# tenant


@login_required
@user_passes_test(lambda u: u.is_staff)
def tenant(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/tenant.html", context)
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


# guest


@login_required
@user_passes_test(lambda u: u.is_staff)
def guest(request):
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/guest.html", context)
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

# request


@login_required
@user_passes_test(lambda u: u.is_staff)
def tenant_request(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/request.html", context)
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

# notifications


@login_required
@user_passes_test(lambda u: u.is_staff)
def notif(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/notifs.html", context)
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

# booking


@login_required
@user_passes_test(lambda u: u.is_staff)
def booking(request):

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        context = {
            'properties': Property.objects.filter(owner_id__user_id=request.user),
            'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
            'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
            'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
            'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
        }
        return render(request, "components/dashboard/booking.html", context)
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

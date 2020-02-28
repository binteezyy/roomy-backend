from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
        properties = Property.objects.filter(owner_id__user_id=request.user)
        context = {
            'properties': properties,
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

# home ajax
def home_ajax(request):
    val = request.GET.get('property', None)
    property_o = Property.objects.filter(owner_id__user_id=request.user, pk=val)
    active_tenants = TenantAccount.objects.filter(transaction_id__active=True, transaction_id__room_id__catalog_id__property_id=property_o).count()
    pending_bookings = Booking.objects.filter(status=0, catalog_id__property_id__owner_id__user_id=request.user, catalog_id__property_id=property_o).count()
    active_rooms = Room.objects.filter(catalog_id__property_id=property_o, is_available=False).count()
    avail_rooms = Room.objects.filter(catalog_id__property_id=property_o, is_available=True).count()
    data = {
        'active_tenants': active_tenants,
        'pending_bookings': pending_bookings,
        'active_rooms': active_rooms,
        'avail_rooms': avail_rooms,
    }
    return JsonResponse(data)

# rental


@login_required
@user_passes_test(lambda u: u.is_staff)
def rental(request):
    next = request.GET.get('next')
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
    next = request.GET.get('next')
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
    next = request.GET.get('next')
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
    next = request.GET.get('next')
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
    next = request.GET.get('next')
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
    next = request.GET.get('next')
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

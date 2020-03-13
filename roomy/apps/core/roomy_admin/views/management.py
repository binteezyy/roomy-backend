from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse  # get_object_or_404

from apps.core.roomy_admin.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.core.roomy_core.models import *
from apps.core.roomy_admin.forms import *

from django.db.models.signals import post_save
from django.dispatch import receiver

context = {
    "title": "Roomy",
}

# property management


@login_required
@user_passes_test(lambda u: u.is_staff)
def property_management(request):
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

# catalog signals
@receiver(post_save, sender=RoomCatalog)
def my_handler(sender, instance, created, **kwargs):
    print('start')

    if created:
        print('catalog created')
        try:
            new_room = Room.objects.get(catalog_id__pk=instance.pk, number=1)
        except Room.DoesNotExist:
            new_room = Room(catalog_id=instance, number=1)
            new_room.save()
        print(new_room)
        try:
            new_fee = Fee.objects.get(property_id=instance.property_id, description=f'{instance.name} rate', amount=instance.rate, fee_type=2)
        except Fee.DoesNotExist:
            new_fee = Fee(property_id=instance.property_id, description=f'{instance.name} rate', amount=instance.rate, fee_type=2)
            new_fee.save()
        print(new_fee)
    else:
        print('update catalog')
        try:
            new_fee = Fee.objects.get(property_id=instance.property_id, description=f'{instance.name} rate', amount=instance.rate, fee_type=2)
        except Fee.DoesNotExist:
            new_fee = Fee(property_id=instance.property_id, description=f'{instance.name} rate', amount=instance.rate, fee_type=2)
            new_fee.save()

        transactions = Transaction.objects.filter(room_id__catalog_id__pk=instance.pk)
        print(transactions)
        for transaction in transactions:
            try:
                old_fee = Fee.objects.exclude(amount=new_fee.amount).get(property_id=instance.property_id, description=f'{instance.name} rate', fee_type=2)
                print(f'OLD FEE {old_fee}')
                transaction.add_ons.remove(old_fee)
                print('add fee')
                transaction.add_ons.add(new_fee)
            except Exception as e:
                print(f' EXCEPTION {e}')

        print(new_fee)
# room management


@login_required
@user_passes_test(lambda u: u.is_staff)
def room_management(request):
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

# owner profile


@login_required
@user_passes_test(lambda u: u.is_staff)
def owner_profile(request):
    next = request.GET.get('next')
    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        user = request.user
        owner_account = OwnerAccount.objects.get(user_id=request.user)
        form1 = UserUpdateForm(request.POST, prefix='user_form')
        form2 = OwnerAccountForm(request.POST, prefix='account_form')

        if request.method == "POST":
            if form1.is_valid() or form2.is_valid():
                print('nice')
                user.username = request.POST.get('id_user_form-username')
                user.first_name = request.POST.get('id_user_form-first_name')
                user.last_name = request.POST.get('id_user_form-last_name')
                user.email = request.POST.get('id_user_form-email')
                user.save()

                owner_account.birthday = request.POST.get(
                    'id_account_form-birthday')
                owner_account.cell_number = request.POST.get(
                    'id_account_form-cell_number')
                owner_account.provincial_address = request.POST.get(
                    'id_account_form-provincial_address')
                owner_account.save()
            else:
                print('invalid form?')

            return redirect('owner-profile')
        else:
            form1 = UserUpdateForm(instance=user, prefix='user_form')
            form2 = OwnerAccountForm(
                instance=owner_account, prefix='account_form')

            context = {
                'properties': Property.objects.filter(owner_id__user_id=request.user),
                'catalogs': RoomCatalog.objects.filter(property_id__owner_id__user_id=request.user),
                'messages': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user).order_by('-time_stamp')[:5],
                'unread': Request.objects.filter(transaction_id__room_id__catalog_id__property_id__owner_id__user_id=request.user, read=False).count(),
                'notifs': OwnerNotification.objects.filter(owner_id__user_id=request.user).order_by('-time_stamp')[:5],
                'unread_notif': OwnerNotification.objects.filter(owner_id__user_id=request.user, read=False).count(),
                'form1': form1,
                'form2': form2,
            }
            return render(request, "components/management/owner_profile.html", context)
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

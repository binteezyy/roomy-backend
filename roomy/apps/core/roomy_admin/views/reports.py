from apps.core.roomy_core.models import *

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse  # get_object_or_404

from apps.core.roomy_admin.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from datetime import datetime, date

import csv, io


@login_required
@user_passes_test(lambda u: u.is_staff)
def generate_report(request):
    next = request.GET.get('next')

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        report_type = request.POST.get('report_type')
        property_o = Property.objects.get(owner_id__user_id=request.user, pk=request.POST.get('select_property'))

        response = HttpResponse(content_type='text/csv')
        if report_type == "Room":
            room_filter = request.POST.get('room_filter')
            response['Content-Disposition'] = 'attachment; filename="list_rooms.csv"'
            writer = csv.writer(response, delimiter=',')

            writer.writerow([f'ROOMS IN PROPERTY - {property_o.name}'])
            catalogs = RoomCatalog.objects.filter(property_id=property_o).order_by('-floor')
            for catalog in catalogs:
                writer.writerow(['CATALOG NAME', 'DESCRIPTION', 'FLOOR', 'RATE'])
                writer.writerow([catalog.name, catalog.description, catalog.floor, catalog.rate])

                writer.writerow(['', f'ROOMS'])
                if room_filter == "active":
                    rooms = Room.objects.filter(catalog_id=catalog).exclude(status=0).order_by('-number')
                elif room_filter == "avail":
                    rooms = Room.objects.filter(catalog_id=catalog, status=0).order_by('-number')
                else:
                    rooms = Room.objects.filter(catalog_id=catalog).order_by('-number')
                writer.writerow(['', 'NUMBER', 'STATUS'])
                for room in rooms:
                    writer.writerow(['', room.number, room.get_status_display()])
            
        elif report_type == "Tenant":
            response['Content-Disposition'] = 'attachment; filename="list_tenants.csv'
            writer = csv.writer(response, delimiter=',')

            tenants = TenantAccount.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o).order_by('-transaction_id__active')
            writer.writerow(['NAME', 'BIRTHDAY', 'CELL NO.', 'ADDRESS', 'CATALOG', 'ROOM', 'STATUS'])
            for tenant in tenants:
                status = ""
                if tenant.transaction_id.active:
                    status = "ACTIVE"
                else:
                    status = "INACTIVE"
                writer.writerow([f'{tenant.user_id.first_name} {tenant.user_id.last_name}', tenant.birthday, tenant.cell_number, tenant.provincial_address, tenant.transaction_id.room_id.catalog_id.name, tenant.transaction_id.room_id.number, status])

        elif report_type == "Payment":
            payment_filter = request.POST.get('payment_filter')
            payment_date = request.POST.get('div_payment_filter_year')
            month, year = payment_date.split('-')
            response['Content-Disposition'] = 'attachment; filename="list_payments.csv'
            writer = csv.writer(response, delimiter=',')

            writer.writerow([f'PAYMENTS IN {property_o.name}'])
            if payment_filter == "Custom":
                billings = Billing.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o, time_stamp__month__gte=month, time_stamp__year__gte=year).order_by('-time_stamp')
            else:
                billings = Billing.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o, time_stamp__month__gte=month, time_stamp__year__gte=year).order_by('-time_stamp')
            
            writer.writerow(['DATE', 'ROOM', 'AMOUNT', 'STATUS'])

            unpaid = 0
            paid = 0
            for billing in billings:
                amount = 0
                status = ""
                for fee in billing.billing_fee.all():
                    amount += int(fee.amount)

                if billing.paid:
                    status = "PAID"
                    paid += amount
                else:
                    status = "UNPAID"
                    unpaid += amount
            writer.writerow([billing.time_stamp, billing.transaction_id.room_id, amount, status])

            writer.writerow(['UNPAID:', f'{unpaid}', 'PAID:', f'{paid}'])

        elif report_type == "Expense":
            expense_filter = request.POST.get('expense_filter')
            expense_date =request.POST.get('div_expense_filter_year')
            month, year = expense_date.split('-')
            response['Content-Disposition'] = 'attachment; filename="list_expenses.csv'
            writer = csv.writer(response, delimiter=',')

            writer.writerow([f'EXPENSES IN {property_o.name}'])
            if expense_filter == "Custom":
                expenses = Expense.objects.filter(property_id=property_o, time_stamp__month__gte=month, time_stamp__year__gte=year)
            else:
                expenses = Expense.objects.filter(property_id=property_o)
            writer.writerow(['DATE', 'DESCRIPTION', 'AMOUNT'])

            total = 0
            for expense in expenses:
                total += int(expense.amount)
                writer.writerow([expense.time_stamp, expense.description, expense.amount])
        
            writer.writerow(['', 'TOTAL:', f'{total}'])

        elif report_type == "Cashflow":
            cashflow_filter = request.POST.get('cashflow_filter')
            cashflow_date =request.POST.get('div_cashflow_filter_year')
            month, year = cashflow_date.split('-')
            response['Content-Disposition'] = 'attachment; filename="cashflow_report.csv'
            writer = csv.writer(response, delimiter=',')

            properties = Property.objects.filter(owner_id__user_id=request.user)
            for property_o in properties:
                writer.writerow(['PROPERTY NAME', 'PROPERTY TYPE', 'PROPERTY DESCRIPTION'])
                writer.writerow([property_o.name, property_o.property_type, property_o.description])
            
                if cashflow_filter == "Custom":
                    billings = Billing.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o, paid=True, time_stamp__month__gte=month, time_stamp__year__gte=year)
                    expenses_o = Expense.objects.filter(property_id=property_o, time_stamp__month__gte=month, time_stamp__year__gte=year)            
                else:
                    billings = Billing.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o, paid=True)
                    expenses_o = Expense.objects.filter(property_id=property_o)
                writer.writerow(['', f'BILLING FOR {date}'])
                billings = Billing.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o, paid=True, time_stamp__month__gte=month, time_stamp__year__gte=year)
                writer.writerow(['', 'DATE', 'ROOM', 'AMOUNT'])
                payments = 0
                for billing in billings:
                    for fee in billing.billing_fee.all():
                        payments += int(fee.amount)
                    writer.writerow(['', billing.time_stamp, billing.transaction_id.room_id, payments])
                writer.writerow(['', '', 'TOTAL:', payments])

                writer.writerow(['', f'EXPENSES FOR {date}'])
                writer.writerow(['', 'DATE', 'DESCRIPTION', 'AMOUNT'])

                expenses = 0
                for expense in expenses_o:
                    expenses += int(expense.amount)
                    writer.writerow(['', expense.time_stamp, expense.description, expense.amount])
                writer.writerow(['', '', 'TOTAL:', expenses])
                networth = payments - expenses
                writer.writerow(['', '', 'NETWORTH:', networth])
                writer.writerow(['', '', '', ''])

        return response
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

@login_required
@user_passes_test(lambda u: u.is_staff)
def list_properties(request):
    next = request.GET.get('next')

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        return HttpResponse("OK")

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

@login_required
@user_passes_test(lambda u: u.is_staff)
def list_rooms(request, pk):
    next = request.GET.get('next')

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        property_o = Property.objects.get(owner_id__user_id=request.user, pk=pk)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="list_rooms.csv'
        writer = csv.writer(response, delimiter=',')

        writer.writerow([f'ROOMS IN PROPERTY - {property_o.name}'])
        catalogs = RoomCatalog.objects.filter(property_id=property_o).order_by('-floor')
        for catalog in catalogs:
            writer.writerow(['CATALOG NAME', 'DESCRIPTION', 'FLOOR', 'RATE'])
            writer.writerow([catalog.name, catalog.description, catalog.floor, catalog.rate])

            writer.writerow(['', f'ROOMS'])
            rooms = Room.objects.filter(catalog_id=catalog).order_by('-number')
            writer.writerow(['', 'NUMBER', 'STATUS'])
            for room in rooms:
                writer.writerow(['', room.number, room.get_status_display()])

        return response
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

@login_required
@user_passes_test(lambda u: u.is_staff)
def list_tenants(request, pk):
    next = request.GET.get('next')

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        property_o = Property.objects.get(owner_id__user_id=request.user, pk=pk)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="list_tenants.csv'
        writer = csv.writer(response, delimiter=',')

        writer.writerow([f'TENANTS IN {property_o.name}'])
        
        tenants = TenantAccount.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o).order_by('-transaction_id__active')
        writer.writerow(['NAME', 'BIRTHDAY', 'CELL NO.', 'ADDRESS', 'CATALOG', 'ROOM', 'STATUS'])
        for tenant in tenants:
            status = ""
            if tenant.transaction_id.active:
                status = "ACTIVE"
            else:
                status = "INACTIVE"
            writer.writerow([f'{tenant.user_id.first_name} {tenant.user_id.last_name}', tenant.birthday, tenant.cell_number, tenant.provincial_address, tenant.transaction_id.room_id.catalog_id.name, tenant.transaction_id.room_id.number, status])

        return response
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

@login_required
@user_passes_test(lambda u: u.is_staff)
def list_payments(request, pk):
    next = request.GET.get('next')

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        property_o = Property.objects.get(owner_id__user_id=request.user, pk=pk)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="list_payments.csv'
        writer = csv.writer(response, delimiter=',')

        writer.writerow([f'PAYMENTS IN {property_o.name}'])
        billings = Billing.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o).order_by('-time_stamp')
        writer.writerow(['DATE', 'ROOM', 'AMOUNT', 'STATUS'])

        unpaid = 0
        paid = 0
        for billing in billings:
            amount = 0
            status = ""
            for fee in billing.billing_fee.all():
                amount += int(fee.amount)

            if billing.paid:
                status = "PAID"
                paid += amount
            else:
                status = "UNPAID"
                unpaid += amount
            writer.writerow([billing.time_stamp, billing.transaction_id.room_id, amount, status])

        writer.writerow(['UNPAID:', f'{unpaid}', 'PAID:', f'{paid}'])
        return response
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

@login_required
@user_passes_test(lambda u: u.is_staff)
def list_expenses(request, pk):
    next = request.GET.get('next')

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        property_o = Property.objects.get(owner_id__user_id=request.user, pk=pk)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="list_payments.csv'
        writer = csv.writer(response, delimiter=',')
        
        writer.writerow([f'EXPENSES IN {property_o.name}'])
        expenses = Expense.objects.filter(property_id=property_o)
        writer.writerow(['DATE', 'DESCRIPTION', 'AMOUNT'])

        total = 0
        for expense in expenses:
            total += int(expense.amount)
            writer.writerow([expense.time_stamp, expense.description, expense.amount])
        
        writer.writerow(['', 'TOTAL:', f'{total}'])
        return response
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

@login_required
@user_passes_test(lambda u: u.is_staff)
def generate_my_cashflow(request, date):
    next = request.GET.get('next')

    if request.user.is_authenticated and OwnerAccount.objects.filter(user_id=request.user).exists():
        month, year = date.split('-')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="month_year_cashflow_report.csv'

        writer = csv.writer(response, delimiter=',')
        properties = Property.objects.filter(owner_id__user_id=request.user)
        for property_o in properties:
            writer.writerow(['PROPERTY NAME', 'PROPERTY TYPE', 'PROPERTY DESCRIPTION'])
            writer.writerow([property_o.name, property_o.property_type, property_o.description])
            
            writer.writerow(['', f'BILLING FOR {date}'])
            billings = Billing.objects.filter(transaction_id__room_id__catalog_id__property_id=property_o, paid=True, time_stamp__month__gte=month, time_stamp__year__gte=year)
            writer.writerow(['', 'DATE', 'ROOM', 'AMOUNT'])
            payments = 0
            for billing in billings:
                for fee in billing.billing_fee.all():
                    payments += int(fee.amount)
                writer.writerow(['', billing.time_stamp, billing.transaction_id.room_id, payments])
            writer.writerow(['', '', 'TOTAL:', payments])

            writer.writerow(['', f'EXPENSES FOR {date}'])
            writer.writerow(['', 'DATE', 'DESCRIPTION', 'AMOUNT'])
            expenses_o = Expense.objects.filter(property_id=property_o, time_stamp__month__gte=month, time_stamp__year__gte=year)
            expenses = 0
            for expense in expenses_o:
                expenses += int(expense.amount)
                writer.writerow(['', expense.time_stamp, expense.description, expense.amount])
            writer.writerow(['', '', 'TOTAL:', expenses])
            networth = payments - expenses
            writer.writerow(['', '', 'NETWORTH:', networth])
            writer.writerow(['', '', '', ''])
        return response
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
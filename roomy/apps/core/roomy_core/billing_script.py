from django.contrib.auth.models import User
from .models import *
from datetime import datetime, date
from django.db.models import Count
from functools import reduce


def billing_create():
    print('BILLING CREATION')
    # get all active transactions - meaning rooms that are occupied by tenants with on going contracts
    transactions = Transaction.objects.filter(active=True)
    # loop through transactions
    for transaction in transactions:
        # get or create billing with this transaction and datetime.month
        if (transaction.billing_date-date.today()).days < 0:
            b_date = date(datetime.now().year, datetime.now().month,
                          transaction.billing_date.day)
            try:
                billing = Billing.objects.get(
                    time_stamp__month=datetime.now().month, transaction_id=transaction)
                print('billing exists')
            except Billing.DoesNotExist:
                billing = Billing(time_stamp=b_date,
                                  transaction_id=transaction)

                fees = []
                for fee in transaction.add_ons.all():
                    fees.append(fee)

                billing.save()
                billing.billing_fee.set(fees)
                print('does not exists')
            # if datetime.now is > 1 week before time stamp and notif does not exist, get or create owner notif to let him adjust
                # ** NOTE THAT THIS BILLING SHOULD NOT BE VISIBLE IN THE CLIENT UI NOT UNTIL TENANT NOTIF ARRIVES
            if (billing.time_stamp - date.today()).days < 7 and billing.paid == False:
                # create notif every day 1 week before billing notif sent to tenant
                print(
                    f'{(billing.time_stamp - date.today()).days} days before billing')
                title = f'New billing for {transaction.room_id.catalog_id.property_id.name}, {transaction.room_id.catalog_id.name}, {transaction.room_id.number}'
                body = f'Please review billing details for Property:{transaction.room_id.catalog_id.property_id.name}, Catalog:{transaction.room_id.catalog_id.name}, Room:{transaction.room_id.number}. URL: localhost:8080/cashflow/billing'
                try:
                    owner_notif = OwnerNotification.objects.get(
                        owner_id=transaction.room_id.catalog_id.property_id.owner_id, title=title, time_stamp=date.today())
                    print('owner notif exists')
                except OwnerNotification.DoesNotExist:
                    owner_notif = OwnerNotification(
                        owner_id=transaction.room_id.catalog_id.property_id.owner_id, title=title, body=body, time_stamp=date.today())
                    owner_notif.save()
                    print('owner notif does not exist')
            # if datetime.now is = 1 day before time stamp, get or create tenant notif for his billing
            if (billing.time_stamp - date.today()).days < 2 and billing.paid == False:
                print(
                    f'{(billing.time_stamp - date.today()).days} days before billing')
                title = f'New billing arrived for {transaction.room_id.catalog_id.property_id.name}, {transaction.room_id.catalog_id.name}, {transaction.room_id.number}!'
                body = f'Please review your billing for {billing.time_stamp}'
                tenants = TenantAccount.objects.filter(
                    transaction_id=transaction)
                for tenant in tenants:
                    try:
                        tenant_notif = Message.objects.get(
                            tenant_id=tenant, title=title, time_stamp=date.today())
                        print('tenant notif exists')
                    except Message.DoesNotExist:
                        tenant_notif = Message(
                            tenant_id=tenant, title=title, body=body, time_stamp=date.today())
                        tenant_notif.save()
                        print('tenant notif does not exist')
        else:
            print('not time yet for billing')

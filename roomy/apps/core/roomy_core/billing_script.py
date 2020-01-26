from django.contrib.auth.models import User
from .models import *
from datetime import datetime
from django.db.models import Count
from functools import reduce

def billing_create():
    ## get all active transactions - meaning rooms that are occupied by tenants with on going contracts
    transactions = Transaction.objects.filter(active=True)

    ## loop through transactions
    # for transaction in transactions:
        ## check every transacction if ther is an existing billing with the same fees(many-to-many) as the transaction
        # billing = Billing.objects.annotate(count=Count('billing_fee')).filter(count=len(transaction.add_ons.all()))
        # billing = reduce(lambda p, id: billing.filter(billing_fee=id), transaction.add_ons.all(), billing)

        ## check if there is an existing for this 
        # billing = Billing.objects.filter(transaction_id=)
        # if billing:
        #     if str(billing[0].time_stamp) < date.now().strftime('%Y-%b-%d'):
        #         print(billing)
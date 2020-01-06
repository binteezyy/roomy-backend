from django.contrib import admin
from .models import *
# Register your models here.

class PostProperty(admin.ModelAdmin):
    list_display = ('name', 'street', 'brgy', 'city')

class PostRoom(admin.ModelAdmin):
    list_display = ('property_id', 'floor', 'number')

class PostTransaction(admin.ModelAdmin):
    list_display = ('active', 'room_id', 'start_date')

class PostUserAccount(admin.ModelAdmin):
    list_display = ('user_type', 'user_id', 'transaction_id')

class PostBilling(admin.ModelAdmin):
    list_display = ('paid', 'time_stamp', 'transaction_id')

class PostFee(admin.ModelAdmin):
    list_display = ('description', 'amount')

class PostRequest(admin.ModelAdmin):
    list_display = ('subject', 'transaction_id')

admin.site.register(Property, PostProperty)
admin.site.register(Room, PostRoom)
admin.site.register(Transaction, PostTransaction)
admin.site.register(Fee, PostFee)
admin.site.register(Billing, PostBilling)
admin.site.register(Request, PostRequest)
admin.site.register(UserAccount, PostUserAccount)
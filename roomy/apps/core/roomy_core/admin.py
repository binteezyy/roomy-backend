from django.contrib import admin
from .models import *
# Register your models here.


class PostProperty(admin.ModelAdmin):
    list_display = ('name', 'street', 'brgy', 'city')


class PostRoom(admin.ModelAdmin):
    list_display = ('property_id', 'floor', 'number')


class PostTransaction(admin.ModelAdmin):
    list_display = ('active', 'room_id', 'start_date')


class PostTenantAccount(admin.ModelAdmin):
    list_display = ('user_id', 'transaction_id')


class PostOwnerAccount(admin.ModelAdmin):
    list_display = ('user_id', )


class PostBilling(admin.ModelAdmin):
    list_display = ('paid', 'time_stamp', 'transaction_id')


class PostFee(admin.ModelAdmin):
    list_display = ('description', 'amount')


class PostRequest(admin.ModelAdmin):
    list_display = ('subject', 'transaction_id', 'time_stamp')


class PostImageFile(admin.ModelAdmin):
    list_display = ('title', 'img_path')


class PostMessage(admin.ModelAdmin):
    list_display = ('user_id', 'transaction_id', 'title', 'sent', 'time_stamp')


class PostBooking(admin.ModelAdmin):
    list_display = ('user_id', 'room_id', 'approved')


class PostGuest(admin.ModelAdmin):
    list_display = ('name', 'transaction_id', 'inside', 'time_stamp')


class PostExpense(admin.ModelAdmin):
    list_display = ('description', 'amount', 'time_stamp')


admin.site.register(Property, PostProperty)
admin.site.register(Room, PostRoom)
admin.site.register(Transaction, PostTransaction)
admin.site.register(Fee, PostFee)
admin.site.register(Billing, PostBilling)
admin.site.register(Request, PostRequest)
admin.site.register(TenantAccount, PostTenantAccount)
admin.site.register(OwnerAccount, PostOwnerAccount)
admin.site.register(ImageFile, PostImageFile)
admin.site.register(Message, PostMessage)
admin.site.register(Document)
admin.site.register(Booking, PostBooking)
admin.site.register(Guest, PostGuest)
admin.site.register(Expense, PostExpense)

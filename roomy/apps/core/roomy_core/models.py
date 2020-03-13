from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.core.exceptions import ValidationError
# Create your models here.


class ImageFile(models.Model):
    title = models.CharField(max_length=32)
    img_path = models.ImageField(
        upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.img_path}'

    class Meta:
        unique_together = ('title', 'img_path')


class OwnerAccount(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    cell_number = models.PositiveIntegerField(null=True, blank=True)
    provincial_address = models.CharField(
        max_length=128, null=True, blank=True)

    def __str__(self):
        return f'Owner: {self.user_id.username} - {self.user_id.first_name} {self.user_id.last_name}'


class Property(models.Model):
    property_type_enum = [
        (0, 'Condominium'),
        (1, 'Apartment'),
        (2, 'Dormitory'),
    ]
    owner_id = models.ForeignKey(
        OwnerAccount, on_delete=models.CASCADE, blank=True, null=True)
    property_type = models.IntegerField(choices=property_type_enum, default=0)
    name = models.CharField(max_length=56, unique=True)
    description = models.TextField(blank=True, null=True)
    property_address = models.CharField(max_length=256, null=True, blank=True)
    property_image = models.ManyToManyField(
        ImageFile, blank=True, related_name='property_image')

    def __str__(self):
        return f'{self.name}, Owner: {self.owner_id.user_id.username} - {self.owner_id.user_id.first_name} {self.owner_id.user_id.last_name}'

    class Meta:
        verbose_name_plural = 'Properties'


class RoomCatalog(models.Model):
    room_type_enum = [
        (0, 'Fixed Rate'),
        (1, 'Submetered'),
    ]

    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=56, blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    floor = models.PositiveIntegerField(default=1)
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    room_type = models.IntegerField(choices=room_type_enum, default=0)
    img_3d = models.ManyToManyField(
        ImageFile, blank=True, related_name='img_3d')
    img_2d = models.ManyToManyField(
        ImageFile, blank=True, related_name='img_2d')

    def __str__(self):
        return f'{self.property_id}: {self.name} Floor {self.floor}'

    class Meta:
        unique_together = ('property_id', 'name')


class Room(models.Model):
    room_status = [
        (0, 'Available'),
        (1, 'Shared'),
        (2, 'Occupied'),
    ]
    catalog_id = models.ForeignKey(
        RoomCatalog, on_delete=models.CASCADE, null=True, blank=True)
    number = models.PositiveIntegerField(default=1)
    status = models.IntegerField(choices=room_status, default=0)

    def __str__(self):
        return f'{self.catalog_id.name} - Room {self.number}'

    class Meta:
        unique_together = ('catalog_id', 'number')


class Fee(models.Model):
    fee_type_enum = [
        (0, 'Miscellaneous Fees'),
        (1, 'Add-ons'),
        (2, 'Room rates'),
    ]
    property_id = models.ForeignKey(
        Property, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=56)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    fee_type = models.IntegerField(choices=fee_type_enum, default=0)

    def __str__(self):
        return f'{self.description}, {self.amount}'

    class Meta:
        unique_together = ('description', 'amount')


class Transaction(models.Model):
    active = models.BooleanField(default=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ], null=True, blank=True)
    rating_description = models.TextField(blank=True, null=True)
    rated = models.BooleanField(default=False)
    add_ons = models.ManyToManyField(Fee, blank=True)
    billing_date = models.DateField(blank=True)

    def __str__(self):
        if self.active:
            return f'Active - {self.room_id}'
        else:
            return f'Inactive - {self.room_id}'


class Billing(models.Model):
    time_stamp = models.DateField(blank=True, null=True)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    billing_fee = models.ManyToManyField(Fee, blank=True)

    def __str__(self):
        return f'{self.paid}, {self.time_stamp}, {self.transaction_id}'

    def is_paid(self):
        if self.paid:
            return "Paid"
        else:
            return "Pending"
    def billing_total(self):
        total = 0
        for y in self.billing_fee.all():
            total += y.amount
        return total
    def get_date(self):
        return self.time_stamp.strftime("%B %d, %Y")
class Request(models.Model):
    r_status = [
        (0, 'Pending'),
        (1, 'Processed'),
        (2, 'Denied'),
    ]
    subject = models.CharField(max_length=56)
    description = models.TextField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=r_status, default=0)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    sent = models.BooleanField(default=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.subject}, {self.transaction_id}, {self.status}'


class Document(models.Model):
    file_path = models.ImageField(upload_to="files")

    def __str__(self):
        return f'{self.file_path}'


class TenantAccount(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    cell_number = models.PositiveIntegerField(null=True, blank=True)
    provincial_address = models.CharField(
        max_length=128, null=True, blank=True)
    transaction_id = models.ForeignKey(
        Transaction, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Tenant: {self.user_id.username} - {self.user_id.first_name} {self.user_id.last_name}'

    def get_bday(self):
        try:
            return self.birthday.strftime("%Y-%m-%d")
        except Exception as e:
            return None

    def save(self, *args, **kwargs):
        if self.transaction_id:
            trans = Transaction.objects.get(pk=self.transaction_id.pk)
            trans.active = True
            trans.save()
        super(TenantAccount, self).save(*args, **kwargs)


class Booking(models.Model):
    status_enum = [
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Denied'),
        (3, 'Cancelledt')
    ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tenant_id = models.ForeignKey(
        TenantAccount, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=56, blank=True, null=True)
    start_date = models.DateField()
    catalog_id = models.ForeignKey(RoomCatalog, on_delete=models.CASCADE)
    document1_id = models.ForeignKey(
        Document, on_delete=models.CASCADE, null=True, blank=True, related_name="document1")
    document2_id = models.ForeignKey(
        Document, on_delete=models.CASCADE, null=True, blank=True, related_name="document2")
    add_ons = models.ManyToManyField(Fee, blank=True)
    status = models.IntegerField(choices=status_enum, default=0)

    def __str__(self):
        return f'Booking: {self.user_id.username} - {self.catalog_id}'

    def save(self, *args, **kwargs):
        if not self.tenant_id:
            if self.status == 1:
                active_transactions = Transaction.objects.filter(
                    active=True, room_id__catalog_id=self.catalog_id)

                avail_room = Room.objects.filter(
                    catalog_id=self.catalog_id, status=0).first()

                try:
                    new_transaction = Transaction.objects.get(
                        active=True, room_id=avail_room)
                except Transaction.DoesNotExist:
                    new_transaction = Transaction(
                        room_id=avail_room, billing_date=self.start_date)
                    new_transaction.save()

                    try:
                        new_fee = Fee.objects.get(property_id=self.catalog_id.property_id,
                                                  description=f'{self.catalog_id.name} rate', amount=self.catalog_id.rate, fee_type=2)
                    except Fee.DoesNotExist:
                        new_fee = Fee(property_id=self.catalog_id.property_id,
                                      description=f'{self.catalog_id.name} rate', amount=self.catalog_id.rate, fee_type=2)
                        new_fee.save()
                    print(new_fee)
                    all_add_ons = []
                    all_add_ons.append(new_fee)
                    for add_on in self.add_ons.all():
                        all_add_ons.append(add_on)
                    new_transaction.add_ons.set(all_add_ons)

                avail_room.status = 2
                avail_room.save()
                print(new_transaction)
                try:
                    new_tenant = TenantAccount.objects.get(
                        user_id=self.user_id, transaction_id=new_transaction)
                except TenantAccount.DoesNotExist:
                    new_tenant = TenantAccount(
                        user_id=self.user_id, transaction_id=new_transaction)
                    new_tenant.save()
                print(new_tenant)

                self.tenant_id = new_tenant
                print(self.tenant_id)

        else:
            print("tenant id and transcation already done")
        super(Booking, self).save(*args, **kwargs)


class Message(models.Model):
    tenant_id = models.ForeignKey(TenantAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    body = models.TextField(blank=True, null=True)
    time_stamp = models.DateField(auto_now_add=True, blank=True, null=True)
    sent = models.BooleanField(default=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tenant_id.user_id.first_name} {self.tenant_id.user_id.last_name}- {self.title} - {self.sent}'


class OwnerNotification(models.Model):
    owner_id = models.ForeignKey(OwnerAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    body = models.TextField(blank=True, null=True)
    time_stamp = models.DateField(auto_now_add=True, blank=True, null=True)
    sent = models.BooleanField(default=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner_id.user_id.first_name} {self.owner_id.user_id.last_name}- {self.title} - {self.sent}'


class Guest(models.Model):
    name = models.CharField(max_length=128)
    time_stamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    inside = models.BooleanField(default=True)

    def __str__(self):
        return f'Guest: {self.name}, {self.transaction_id}, In: {self.inside} - {self.time_stamp}'


class Expense(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    time_stamp = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=56)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'Expense - {self.description}, {self.amount}'

    class Meta:
        unique_together = ('description', 'amount')

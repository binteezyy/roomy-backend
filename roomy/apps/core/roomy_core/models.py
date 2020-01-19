from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
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
    birthday = models.DateTimeField(null=True, blank=True)
    cell_number = models.PositiveIntegerField(null=True, blank=True)
    provincial_address = models.CharField(
        max_length=128, null=True, blank=True)

    def __str__(self):
        return f'Owner: {self.user_id.username} - {self.user_id.first_name} {self.user_id.last_name}'


class Property(models.Model):
    property_type_enum = [
        (0, 'Condomenium'),
        (1, 'Dormitory'),
        (2, 'Apartment'),
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


class Room(models.Model):
    room_type_enum = [
        (0, 'Fixed Rate'),
        (1, 'Submetered'),
    ]

    name = models.CharField(max_length=56)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    floor = models.PositiveIntegerField(default=1)
    number = models.PositiveIntegerField(default=1)
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    room_type = models.IntegerField(choices=room_type_enum, default=0)
    image_3d = models.ManyToManyField(
        ImageFile, blank=True, related_name='images_3d')
    image_2d = models.ManyToManyField(
        ImageFile, blank=True, related_name='images_2d')

    def __str__(self):
        return f'{self.property_id}: Floor {self.floor} - Room {self.number}'

    class Meta:
        unique_together = ('property_id', 'floor', 'number')


class Fee(models.Model):
    fee_type_enum = [
        (0, 'Misc Fees'),
        (1, 'Add-ons'),
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
    start_date = models.DateTimeField(null=True, auto_now_add=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ], null=True, blank=True)
    rating_description = models.TextField(blank=True, null=True)
    rated = models.BooleanField(default=False)
    add_ons = models.ManyToManyField(Fee, blank=True)

    def __str__(self):
        if self.active:
            return f'Active - {self.room_id}'
        else:
            return f'Inactive - {self.room_id}'


class Billing(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    billing_fee = models.ManyToManyField(Fee, blank=True)

    def __str__(self):
        return f'{self.paid}, {self.time_stamp}, {self.transaction_id}'


class Request(models.Model):
    subject = models.CharField(max_length=56)
    description = models.TextField(blank=True, null=True)
    time_stamp = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject}, {self.transaction_id}, {self.status}'


class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.ForeignKey(
        Transaction, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=32)
    body = models.TextField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    sent = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_id.username} - {self.title} - {self.sent}'


class Document(models.Model):
    file_path = models.ImageField(upload_to="files")

    def __str__(self):
        return f'{self.file_path}'


class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    document1_id = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="document1")
    document2_id = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="document2")
    add_ons = models.ManyToManyField(Fee, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Booking: {self.user_id.username} - {self.room_id}'


class TenantAccount(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateTimeField(null=True, blank=True)
    cell_number = models.PositiveIntegerField(null=True, blank=True)
    provincial_address = models.CharField(
        max_length=128, null=True, blank=True)
    transaction_id = models.ForeignKey(
        Transaction, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Tenant: {self.user_id.username} - {self.user_id.first_name} {self.user_id.last_name}'


class Guest(models.Model):
    name = models.CharField(max_length=128)
    time_stamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    inside = models.BooleanField(default=True)

    def __str__(self):
        return f'Guest: {self.name}, {self.transaction_id}, In: {self.inside} - {self.time_stamp}'


class Expense(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()
    description = models.CharField(max_length=56)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'Expense - {self.description}, {self.amount}'

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=56, unique=True)
    street = models.CharField(max_length=56)
    brgy = models.CharField(max_length=56)
    city = models.CharField(max_length=56)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        unique_together = ('name', 'street', 'brgy', 'city')

class Room(models.Model):
    room_type_enum = [
        (0, 'Fixed Rate'),
        (1, 'Submetered'),
    ]
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    floor = models.PositiveIntegerField(default=1)
    number = models.PositiveIntegerField(default=1)
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    room_type = models.IntegerField(choices=room_type_enum, default=0)

    def __str__(self):
        return f'{self.property_id}, Floor {self.floor}, Room {self.number}'

    class Meta:
        unique_together = ('property_id', 'floor', 'number')

class Transaction(models.Model):
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, auto_now_add=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.active}, {self.room_id}'

class Fee(models.Model):
    description = models.CharField(max_length=56)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'{self.description}, {self.amount}'

    class Meta:
        unique_together = ('description', 'amount')

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
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject}, {self.transaction_id}'
        
class UserAccount(models.Model):
    user_type_enum = [
        (0, 'Tennant'),
        (1, 'Owner/Manager'),
    ]
    user_type = models.IntegerField(choices=user_type_enum, default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_user_type_display()} {self.user_id.username}, {self.transaction_id}'
from django.db      import models

# CUSTOM MODELS
from phonenumber_field.modelfields      import PhoneNumberField

class ContactUs(models.Model):
    name = models.CharField(max_length=56, unique=True)
    email = models.EmailField(max_length=40)
    phone_number = PhoneNumberField()
    message = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label="client"

class OwnerApplication(models.Model):
    name = models.CharField(max_length=56, unique=True)
    company = models.CharField(max_length=56, unique=True)
    email = models.EmailField(max_length=40)
    phone_number = PhoneNumberField()
    message = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label="client"

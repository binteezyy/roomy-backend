from django.db                      import models
from django.contrib.auth.models     import User
# CUSTOM MODELS
from phonenumber_field.modelfields      import PhoneNumberField

class ContactUs(models.Model):
    name = models.CharField(max_length=56)
    email = models.EmailField(max_length=40)
    phone_number = PhoneNumberField()
    message = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label="client"

class OwnerApplication(models.Model):
    name = models.CharField(max_length=56)
    company = models.CharField(max_length=56)
    email = models.EmailField(max_length=40)
    phone_number = PhoneNumberField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    class Meta:
        unique_together = ('name','email')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label="client"

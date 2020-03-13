from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from apps.core.roomy_core.models import *
from bootstrap_modal_forms.forms import BSModalForm
from phonenumber_field.formfields import PhoneNumberField
from .models.application import *
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email',max_length=254)
    email2 = forms.EmailField(label='Confirm Email',max_length=254)
    password = forms.CharField(widget=forms.PasswordInput, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

    def cleaned_data(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        username = self.cleaned_data.get('username')

        if email != email2:
            raise forms.ValidationError("Emails does not match")

        username_q = User.objects.filter(username=username)
        email_q = User.objects.filter(username=email)
        if username_q.exists():
            raise forms.ValidationError("Username already registered")
        elif email_q.exists():
            raise forms.ValidationError("Email already registered")

        return super(UserRegisterForm, self).clean(*args, **kwargs)


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email',max_length="254")
    phone_number = PhoneNumberField()
    message = forms.CharField(label='Message',widget=forms.Textarea(attrs={"rows":"5", "cols":"20"}))

    class Meta:
        model = ContactUs
        fields = [
            'name',
            'email',
            'phone_number',
            'message'
        ]

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')
        message = cleaned_data.get('message')

        print("CONTACT SUBMISSION")
        print("NAME:",name)
        print("EMAIL:",email)
        print("PHONE NUMBER:",phone_number)
        print("MESSAGE:",message)
        return super(ContactUsForm, self).clean(*args, **kwargs)

class OwnerApplicationForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', required=True)
    company = forms.CharField(label='Company', required=True)
    email = forms.EmailField(label='Email',max_length=254, required=True)
    phone_number = PhoneNumberField()

    class Meta:
        model = OwnerApplication
        fields = [
            'full_name',
            'company',
            'email',
            'phone_number',
        ]

class RoomRequestForm(forms.ModelForm):
    message = forms.CharField(label='Message',widget=forms.Textarea(attrs={"rows":"5", "cols":"20"}))
    class Meta:
        model = OwnerApplication
        fields = [
            'message',
        ]
        
    def cleaned_data(self, *args, **kwargs):
        message = self.cleaned_data.get('message')

        return super(RoomRequestForm, self).clean(*args, **kwargs)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from apps.core.roomy_core.models import *
from bootstrap_modal_forms.forms import BSModalForm


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('User does not exist')

        if not user.check_password(password):
            raise forms.ValidationError('Incorrect password')

        if user and password:
            user = authenticate(username=username, password=password)

            if not user.is_active:
                raise forms.ValidationError('User is not active')

            print("VALID USER:",user)
            return self.cleaned_data
        return super(UserLoginForm, self).clean(*args, **kwargs)

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean(self, *args, **kwargs):
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


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
class OwnerAccountForm(forms.ModelForm):
    class Meta:
        model = OwnerAccount
        exclude = ['user_id']
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts                   import render, get_object_or_404, redirect, reverse
from django.contrib import auth
# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def login(request):
    context.update({
        "form": AuthenticationForm,
    })
    return render(request,"web/components/login.html",context)

def logout(request):
    auth.logout(request)
    return redirect('home')

def forgot_password(request):
    return render(request,"web/components/forgot_password.html",context)

def sign_up(request):
    return render(request,"web/components/sign_up.html",context)

def get_in_touch(request):
    return render(request,"web/components/get_in_touch.html",context)

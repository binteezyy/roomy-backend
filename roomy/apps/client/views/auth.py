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
    return render(request,"components/login.html",context)

def logout(request):
    auth.logout(request)
    return redirect('home')

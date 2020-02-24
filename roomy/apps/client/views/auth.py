from django.shortcuts               import render
from django.contrib.auth.forms      import AuthenticationForm
from django.shortcuts               import render, get_object_or_404, redirect, reverse
from apps.core.roomy_admin.forms    import UserLoginForm
from django.contrib                 import auth,messages
from django.contrib.auth            import authenticate, logout, login
from ..forms                        import *


from django.contrib.auth.models import User
# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def clogin(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST' and form.is_valid():
        form.clean()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context.update({
        "TITLE": "Login",
        "form": form,
    })
    # if request.method == 'POST'
    return render(request,"web/components/login.html",context)

def clogout(request):
    auth.logout(request)
    return redirect('home')

def cforgot_password(request):
    return render(request,"web/components/forgot_password.html",context)

def csign_up(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            raw_password = form.cleaned_data.get('password')
            user.set_password(raw_password)
            user.save()
            try:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            except Exception as e:
                User.objects.get(username=username).delete()
                raise
            return redirect('home')

        else:
            form_error = True
    context.update({
        "TITLE": "Sign Up",
        "form": form,
    })
    return render(request,"web/components/sign_up.html",context)

def get_in_touch(request):
    form = OwnerApplicationForm(request.POST or None)
    if request.method == 'POST':
        print("POST")
        if form.is_valid():
            form.cleaned_data()
            full_name = form.cleaned_data.get('full_name')
            company = form.cleaned_data.get('company')
            print("wow")
        else:
            messages.error(request, "Error")
    else:
        pass
    context.update({
        "TITLE": "Partner With US!",
        "form": form,
    })
    return render(request,"web/components/get_in_touch.html",context)

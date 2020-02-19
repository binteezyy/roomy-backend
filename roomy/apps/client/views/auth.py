from django.shortcuts               import render
from django.contrib.auth.forms      import AuthenticationForm
from django.shortcuts               import render, get_object_or_404, redirect, reverse
from apps.core.roomy_admin.forms    import UserLoginForm, UserRegisterForm
from django.contrib                 import auth,messages
from django.contrib.auth            import authenticate, logout, login as clogin
# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def login(request):
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
            clogin(request, user)
            return redirect('home')

    context.update({
        "TITLE": "Login",
        "form": form,
    })
    # if request.method == 'POST'
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

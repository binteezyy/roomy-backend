from django.conf                    import settings
from django.shortcuts               import render
from django.contrib.auth.forms      import AuthenticationForm
from django.shortcuts               import render, get_object_or_404, redirect, reverse
from apps.core.roomy_admin.forms    import UserLoginForm
from django.contrib                 import auth,messages
from django.contrib.auth            import authenticate, logout, login
from ..forms                        import *
from apps.commons.views.apis        import recaptcha_verify
from apps.client.models.application import OwnerApplication
from django.contrib.auth.models     import User
from django.http                    import HttpResponseRedirect
from django.http                    import HttpResponse
from django.contrib                 import messages

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
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/login.html",context)
    else:
        return render(request,"web/components/login.html",context)

def clogout(request):
    auth.logout(request)

    return redirect(request.META.get('HTTP_REFERER', 'index'))

def cforgot_password(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/forgot_password.html",context)
    else:
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
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/sign_up.html",context)
    else:
        return render(request,"web/components/sign_up.html",context)

def get_in_touch(request):
    form = OwnerApplicationForm(request.POST or None)
    if request.method == 'POST':

        recaptcha = False
        try:
            recaptcha = recaptcha_verify(request.POST["g-recaptcha-response"])['success']
        except Exception as e:
            pass
        if form.is_valid() and recaptcha:
            full_name = form.clean.get('full_name')
            company = form.clean.get('company')
            email = form.clean.get('email')
            phone_number = form.clean.get('phone_number')

            user_ = None
            if request.user.is_authenticated:
                user_ = request.user

            try:
                application = OwnerApplication.objects.create(
                name = full_name,
                company = company,
                email = email,
                phone_number = phone_number,
                user = user_
                )
            except Exception as e:
                raise

            messages.add_message(request, messages.INFO, 'Succesfully submitted Owner Application, our staff will get to you soon')
            return redirect('home')
        else:
            pass

    context.update({
        "TITLE": "Partner With US!",
        "form": form,
        "RECAPTCHA_KEY": settings.RECAPTCHA_KEY,
        "form_type": "owner-application",
    })
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/get_in_touch.html",context)
    else:
        return render(request,"web/components/get_in_touch.html",context)

def modal_auth(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.clean()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(request.META.get('HTTP_REFERER', 'index'))
        else:
            #RETURN ERROR MESSAGE
            return redirect(request.META.get('HTTP_REFERER', 'index'))
    else:
        context.update({
            "TITLE": "Login",
            "form": form,
        })
        if request.user_agent.device.family == "Roomy Native":
            return render(request,"mobile-native/components/modals/authenticate.html",context)
        else:
            return render(request,"web/components/modals/authenticate.html",context)

def owner_application_submit(request):
    context.update({

    })
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/modals/submit+recaptcha.html",context)
    else:
        return render(request,"web/components/modals/submit+recaptcha.html",context)

def authListener(request):
    if request.user.is_authenticated: 
        return HttpResponse("[{\"username\" : \"" + request.user.username + "\",\"first_name\" : \"" + request.user.first_name + "\"}]")
    else:
        return HttpResponse("[{\"username\" : \"0\",\"first_name\" : \"Guest\"}]")
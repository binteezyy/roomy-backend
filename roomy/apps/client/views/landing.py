from django.shortcuts                               import render
from django.core.paginator                          import Paginator
from django.shortcuts                               import render, get_object_or_404, redirect, reverse
from django.contrib                                 import messages
from apps.core.roomy_core.models                    import *
from apps.commons.views.apis                        import recaptcha_verify
from django.conf                                    import settings
from django.urls                                    import resolve
from ..models.site                                  import *
from ..forms                                        import *
from webpush                                        import send_user_notification
from ..emails                                       import ContactUs_Handler
from django.contrib.auth.decorators                 import login_required
webpush = {"group": "my_group" }

context = {
    "TITLE": "Roomy",
    "webpush":webpush,
}
def home(request):
    condos = RoomCatalog.objects.filter(property_id__property_type=0).order_by('?')[:6]
    apartments = RoomCatalog.objects.filter(property_id__property_type=1).order_by('?')[:6]
    dorms = RoomCatalog.objects.filter(property_id__property_type=2).order_by('?')[:6]

    current_url = resolve(request.path_info).url_name


    try:
        payload = {"head": "Welcome to Roomy!", "body": f"Hi {request.user.first_name}, start booking apps now!","url": current_url}
        send_user_notification(user=request.user, payload=payload, ttl=1000)
    except Exception as e:
        pass
    print("USER_AGENT:",request.user_agent)
    if request.user_agent.device.family == "Roomy Native":
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            context.update({
                "dorms":dorms,
                "condos":condos,
                "apartments":apartments
            })
            return render(request,"mobile-native/components/landing/home.html",context)
    else:
        context.update({
            "dorms":dorms,
            "condos":condos,
            "apartments":apartments
        })
        return render(request,"web/components/landing/home.html",context)

def partner_with_us(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/landing/partner_with_us.html",context)
    else:
        return render(request,"web/components/landing/partner_with_us.html",context)

def about(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/landing/about.html",context)
    else:
        return render(request,"web/components/landing/about.html",context)

def faq(request):
    faqs = FAQ.objects.all().order_by('order')
    paginator = Paginator(faqs, 10)#pagination
    page = request.GET.get('page')
    faqs = paginator.get_page(page)#pagintation end
    context.update({
        "faqs": faqs
    })

    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/landing/faq.html",context)
    else:
        return render(request,"web/components/landing/faq.html",context)

def modal_contact(request):
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


def contact(request):
    form = ContactUsForm(request.POST or None)

    if request.method == "POST":
        recaptcha = False
        try:
            recaptcha = recaptcha_verify(request.POST["g-recaptcha-response"])['success']
        except Exception as e:
            pass
        if form.is_valid():
            form.clean()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            message = form.cleaned_data.get('message')

            try:
                contact_us = ContactUs.objects.create(
                    name = name,
                    email = email,
                    phone_number = phone_number,
                    message = message
                )

                contact_us.save()
                ContactUs_Handler(name,email,phone_number,message)
                messages.success(request, 'Thank you for your feedback! We will be reviewing it later.')
            except Exception as e:
                print("CONTACT FORM ERROR OCCURED:",e)
                contact_us.delete()
                messages.success(request, 'Something went wrong 😞')
                # TODO: CONTACT FORM ERROR HANDLING
        else:
            print("WEW")

    context.update({
        "form": form,
        "RECAPTCHA_KEY": settings.RECAPTCHA_KEY,
    })
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/landing/contact.html",context)
    else:
        return render(request,"web/components/landing/contact/base.html",context)

def terms_of_use(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/landing/terms_of_use.html",context)
    else:
        return render(request,"web/components/landing/terms_of_use.html",context)

def privacy(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/landing/privacy.html",context)
    else:
        return render(request,"web/components/landing/privacy.html",context)

def page_not_found(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/landing/privacy.html",context)
    else:
        return render(request,"web/components/404.html",context)

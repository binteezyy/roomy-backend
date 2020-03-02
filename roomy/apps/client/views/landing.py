from django.shortcuts import render
from apps.core.roomy_core.models import *
context = {
    "TITLE": "Roomy"
}
def home(request):
    dorms = Room.objects.filter(catalog_id__room_type=1)
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/home.html",context)
    else:
        context.update({
            "dorms":dorms,
        })
        return render(request,"web/components/landing/home.html",context)


def booking_guide(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/booking_guide.html",context)
    else:
        return render(request,"web/components/landing/booking_guide.html",context)

def partner_with_us(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/partner_with_us.html",context)
    else:
        return render(request,"web/components/landing/partner_with_us.html",context)

def about(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/about.html",context)
    else:
        return render(request,"web/components/landing/about.html",context)

def faq(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/faq.html",context)
    else:
        return render(request,"web/components/landing/faq.html",context)

def contact(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/contact.html",context)
    else:
        return render(request,"web/components/landing/contact.html",context)

def terms_of_use(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/terms_of_use.html",context)
    else:
        return render(request,"web/components/landing/terms_of_use.html",context)

def privacy(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/privacy.html",context)
    else:
        return render(request,"web/components/landing/privacy.html",context)

def help_center(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/help_center.html",context)
    else:
        return render(request,"web/components/landing/help_center.html",context)

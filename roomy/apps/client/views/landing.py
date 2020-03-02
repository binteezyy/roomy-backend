from django.shortcuts import render
from apps.core.roomy_core.models import *
context = {
    "TITLE": "Roomy"
}
def home(request):
    dorms = Room.objects.filter(catalog_id__room_type=1)
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/base.html",context)
    else:
        context.update({
            "dorms":dorms,
        })
        return render(request,"web/components/landing/home.html",context)


def booking_guide(request):
    return render(request,"web/components/landing/booking_guide.html",context)

def partner_with_us(request):

    return render(request,"web/components/landing/partner_with_us.html",context)

def about(request):
    return render(request,"web/components/landing/about.html",context)

def faq(request):
    return render(request,"web/components/landing/faq.html",context)

def contact(request):
    return render(request,"web/components/landing/contact.html",context)

def terms_of_use(request):
    return render(request,"web/components/landing/terms_of_use.html",context)

def privacy(request):
    return render(request,"web/components/landing/privacy.html",context)

def help_center(request):
    return render(request,"web/components/landing/help_center.html",context)

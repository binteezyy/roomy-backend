from django.shortcuts import render
from apps.core.roomy_core.models import *
from django.urls import resolve

from webpush import send_user_notification
webpush = {"group": "my_group" }

context = {
    "TITLE": "Roomy",
    "webpush":webpush,
}
def home(request):
    dorms = Room.objects.filter(catalog_id__room_type=1)

    current_url = resolve(request.path_info).url_name
    payload = {"head": "Welcome to Roomy!", "body": f"Hi {request.user.first_name}, start booking apps now!","url": current_url}
    send_user_notification(user=request.user, payload=payload, ttl=1000)
    print("USER_AGENT:",request.user_agent)
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

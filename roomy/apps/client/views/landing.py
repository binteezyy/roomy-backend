from django.shortcuts import render
from django.core.paginator                          import Paginator
from apps.core.roomy_core.models import *
from ..models.site import *
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
    try:
        payload = {"head": "Welcome to Roomy!", "body": f"Hi {request.user.first_name}, start booking apps now!","url": current_url}
        send_user_notification(user=request.user, payload=payload, ttl=1000)
    except Exception as e:
        pass
    print("USER_AGENT:",request.user_agent)
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
    faqs = FAQ.objects.all().order_by('order')
    paginator = Paginator(faqs, 10)#pagination
    page = request.GET.get('page')
    faqs = paginator.get_page(page)#pagintation end
    context.update({
        "faqs": faqs
    })
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/faq.html",context)
    else:
        return render(request,"web/components/landing/faq.html",context)

def contact(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/contact.html",context)
    else:
        return render(request,"web/components/landing/contact.html",context)

def team(request):
    if request.user_agent.is_mobile:
        return render(request,"mobile-native/components/landing/team.html",context)
    else:
        return render(request,"web/components/landing/team.html",context)

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

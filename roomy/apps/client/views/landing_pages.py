from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def home(request):
    return render(request,"components/landing_pages/home.html",context)

def explore(request):
    return render(request,"components/landing_pages/explore.html",context)

def booking_guide(request):
    return render(request,"components/landing_pages/booking_guide.html",context)

def partner_with_us(request):
    return render(request,"components/landing_pages/partner_with_us.html",context)

def about(request):
    return render(request,"components/landing_pages/about.html",context)

def faq(request):
    return render(request,"components/landing_pages/faq.html",context)

def contact(request):
    return render(request,"components/landing_pages/contact.html",context)

def terms_of_use(request):
    return render(request,"components/landing_pages/terms_of_use.html",context)

def privacy(request):
    return render(request,"components/landing_pages/privacy.html",context)

def help_center(request):
    return render(request,"components/landing_pages/help_center.html",context)

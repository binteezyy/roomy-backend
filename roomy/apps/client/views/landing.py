from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def explore(request):
    return render(request,"components/landing/explore.html",context)

def booking_guide(request):
    return render(request,"components/landing/booking_guide.html",context)

def partner_with_us(request):
    return render(request,"components/landing/partner_with_us.html",context)

def about(request):
    return render(request,"components/landing/about.html",context)

def faq(request):
    return render(request,"components/landing/faq.html",context)

def contact(request):
    return render(request,"components/landing/contact.html",context)

def terms_of_use(request):
    return render(request,"components/landing/terms_of_use.html",context)

def privacy(request):
    return render(request,"components/landing/privacy.html",context)

def help_center(request):
    return render(request,"components/landing/help_center.html",context)

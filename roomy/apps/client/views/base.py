from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def explore(request):
    return render(request,"components/navigation/explore.html",context)

def about(request):
    return render(request,"components/navigation/about.html",context)

def faq(request):
    return render(request,"components/navigation/faq.html",context)

def contact(request):
    return render(request,"components/navigation/contact.html",context)

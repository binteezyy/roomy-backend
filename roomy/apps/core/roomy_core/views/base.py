from django.http                        import HttpResponse
from django.shortcuts                   import render #get_object_or_404, redirect, reverse
from ..billing_script import *
context = {
    "title": "Roomy",
}

def index(request):
    
    return render(request,"components/base.html",context)

def test_script(request):

    billing_create(request)

    return HttpResponse("script went through")
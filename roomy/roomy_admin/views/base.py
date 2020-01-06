from django.http                        import HttpResponse
from django.shortcuts                   import render #get_object_or_404, redirect, reverse

context = {
    "title": "Roomy",
}

def index(request):

    return render(request,"components/base.html",context)

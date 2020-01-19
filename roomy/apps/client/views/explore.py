from django.shortcuts import render

context = {
    "TITLE": "Roomy — Explore",
    "viewtype": "explore"
}

def index(request):

    return render(request,"components/landing/explore/base.html",context)

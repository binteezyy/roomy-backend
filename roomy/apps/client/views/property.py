from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def room(request):
    return render(request,"components/property/room.html", context)

def amenities(request):
    return render(request,"components/property/amenities.html", context)

def photos(request):
    return render(request,"components/property/photos.html", context)

def rates(request):
    return render(request,"components/property/photos.html", context)

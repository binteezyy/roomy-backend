from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def rooms(request):
    return render(request,"components/property/rooms.html", context)

def amenities(request):
    return render(request,"components/property/amenities.html", context)

def photos(request):
    return render(request,"components/property/photos.html", context)

from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def property(request):
    return render(request,"components/property/property.html", context)

def room(request):
    return render(request,"components/property/room.html", context)

def amenities(request):
    return render(request,"components/property/amenities.html", context)

def photos(request):
    return render(request,"components/property/photos.html", context)

def booking(request):
    return render(request,"components/property/booking.html", context)

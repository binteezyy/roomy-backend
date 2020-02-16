from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def property(request):
    return render(request,"web/components/property/property.html", context)

def amenities(request):
    return render(request,"web/components/property/amenities.html", context)

def photos(request):
    return render(request,"web/components/property/photos.html", context)

def booking(request):
    return render(request,"web/components/property/booking.html", context)

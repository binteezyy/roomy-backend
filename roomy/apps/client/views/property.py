from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def property(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/property/property.html", context)
    else:
        return render(request,"web/components/property/property.html", context)

def amenities(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/property/amenities.html", context)
    else:
        return render(request,"web/components/property/amenities.html", context)

def photos(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/property/photos.html", context)
    else:
        return render(request,"web/components/property/photos.html", context)

def booking(request):
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/property/booking.html", context)
    else:
        return render(request,"web/components/property/booking.html", context)

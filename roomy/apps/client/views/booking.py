from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def booking(request):
    return render(request,"components/booking/booking.html",context)

def booking_step_2(request):
    return render(request,"components/booking/booking_step_2.html",context)

def booking_step_3(request):
    return render(request,"components/booking/booking_step_3.html",context)

def booking_step_4(request):
    return render(request,"components/booking/booking_step_4.html",context)

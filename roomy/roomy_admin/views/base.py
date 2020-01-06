from django.http                        import HttpResponse
from django.shortcuts                   import render #get_object_or_404, redirect, reverse

context = {
    "title": "Roomy",
}

def index(request):

    return render(request,"",context)

# home
def home(request):

    return render(request,"components/home.html",context)

# transaction
def transaction(request):

    return render(request,"components/transaction.html",context)

# rental
def rental(request):

    return render(request,"components/rental.html",context)

# tenant
def tenant(request):

    return render(request,"components/tenant.html",context)

# payment
def payment(request):

    return render(request,"components/payment.html",context)

# expense
def expense(request):

    return render(request,"components/expense.html",context)

# cashflow
def cashflow(request):

    return render(request,"components/cashflow.html",context)

# report
def report(request):

    return render(request,"components/report.html",context)

# property-management
def property_management(request):

    return render(request,"components/property-management.html",context)

# room-management
def room_management(request):

    return render(request,"components/room-management.html",context)

# admin-management
def admin_management(request):

    return render(request,"components/admin_management.html",context)

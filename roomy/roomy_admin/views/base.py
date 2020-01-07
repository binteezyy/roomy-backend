from django.http                        import HttpResponse
from django.shortcuts                   import render #get_object_or_404, redirect, reverse

context = {
    "title": "Roomy",
}

def index(request):

    return render(request,"",context)

# home
def dashboard(request):

    return render(request,"components/dashboard.html",context)

# add_property
def add_property(request):

    return render(request,"components/add_property.html",context)

# add_rental
def add_rental(request):

    return render(request,"components/add_rental.html",context)

# add_payment
def add_payment(request):

    return render(request,"components/add_payment.html",context)

# add_expense
def add_expense(request):

    return render(request,"components/add_expense.html",context)

# rental
def rental(request):

    return render(request,"components/rental.html",context)

# tenant
def tenant(request):

    return render(request,"components/tenant.html",context)

# billing
def billing(request):

    return render(request,"components/billing.html",context)

# expense
def expense(request):

    return render(request,"components/expense.html",context)

# cashflow
def cashflow(request):

    return render(request,"components/cashflow.html",context)

# report
def report(request):

    return render(request,"components/report.html",context)

# property_management
def property_management(request):

    return render(request,"components/property_management.html",context)

# room_management
def room_management(request):

    return render(request,"components/room_management.html",context)

# admin_management
def admin_management(request):

    return render(request,"components/admin_management.html",context)

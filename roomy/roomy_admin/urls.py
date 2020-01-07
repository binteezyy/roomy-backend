from django.urls import path,include
from django.conf.urls.static import static
from .views import base
urlpatterns = [
    path('dashboard/',      base.dashboard,                                        name='dashboard'),
    path('transaction/add_property/',      base.add_property,                                        name='add_property'),
    path('transaction/add_rental/',      base.add_rental,                                        name='add_rental'),
    path('transaction/add_payment/',      base.add_payment,                                        name='add_payment'),
    path('transaction/add_expense/',      base.add_expense,                                        name='add_expense'),
    path('rental/',      base.rental,                                        name='rental'),
    path('tenant/',      base.tenant,                                        name='tenant'),
    path('billing/',      base.billing,                                        name='billing'),
    path('expense/',      base.expense,                                        name='expense'),
    path('cashflow/',      base.cashflow,                                        name='cashflow'),
    path('report/',      base.report,                                        name='report'),
    path('property_management/',      base.property_management,                                        name='property_management'),
    path('room_management/',      base.room_management,                                        name='room_management'),
    path('admin_management/',      base.admin_management,                                        name='admin_management'),
]

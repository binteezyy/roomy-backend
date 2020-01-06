from django.urls import path,include
from django.conf.urls.static import static
from .views import base
urlpatterns = [
    path('dashboard/',      base.dashboard,                                        name='dashboard'),
    path('transaction/',      base.transaction,                                        name='transaction'),
    path('rental/',      base.rental,                                        name='rental'),
    path('tenant/',      base.tenant,                                        name='tenant'),
    path('payment/',      base.payment,                                        name='payment'),
    path('expense/',      base.expense,                                        name='expense'),
    path('cashflow/',      base.cashflow,                                        name='cashflow'),
    path('report/',      base.report,                                        name='report'),
    path('property-management/',      base.property_management,                                        name='property-management'),
    path('room-management/',      base.room_management,                                        name='room-management'),
    path('admin-management/',      base.admin_management,                                        name='admin-management'),
]

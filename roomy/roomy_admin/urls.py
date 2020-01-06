from django.urls import path,include
from django.conf.urls.static import static
from .views import base
urlpatterns = [
    path('home/',      base.home,                                        name='home'),
    path('transaction/',      base.transaction,                                        name='transaction'),
    path('rental/',      base.rental,                                        name='rental'),
    path('tenant/',      base.tenant,                                        name='tenant'),
    path('payment/',      base.payment,                                        name='payment'),
    path('expense/',      base.expense,                                        name='expense'),
    path('cashflow/',      base.cashflow,                                        name='cashflow'),
    path('report/',      base.report,                                        name='report'),
]

from django.urls import path, include
from django.conf.urls.static import static
from .views import base, datatableviews, modalviews
urlpatterns = [
    path('demo/<str:place>', base.demo, name='demo'),
    path('dashboard/',      base.dashboard,
         name='dashboard'),
    path('transaction/add_property/',      base.add_property,
         name='add_property'),
    path('transaction/add_room/',      base.add_room,
         name='add_room'),
    path('transaction/add_rental/',      base.add_rental,
         name='add_rental'),
    path('transaction/add_billing/',      base.add_billing,
         name='add_billing'),
    path('transaction/add_expense/',      base.add_expense,
         name='add_expense'),
    path('transaction/add_admin/',      base.add_admin,
         name='add_admin'),
    path('rental/',      base.rental,
         name='rental'),
    path('tenant/',      base.tenant,
         name='tenant'),
    path('billing/',      base.billing,
         name='billing'),
    path('fee/',      base.fee,
         name='fee'),
    path('expense/',      base.expense,
         name='expense'),
    path('cashflow/',      base.cashflow,
         name='cashflow'),
    path('report/',      base.report,
         name='report'),
    path('property_management/',      base.property_management,
         name='property_management'),
    path('room_management/',      base.room_management,
         name='room_management'),
    path('admin_management/',      base.admin_management,
         name='admin_management'),

    # Data Table Paths
    # Billing Table
    path('billing/table/', datatableviews.billing_table,
         name='admin-billing-table'),
    path('read/billing/<int:pk>',
         modalviews.BillingReadModal.as_view(), name='read-billing'),
    path('delete/billing/<int:pk>',
         modalviews.BillingDeleteModal.as_view(), name='delete-billing'),
    path('update/billing/<int:pk>',
         modalviews.BillingUpdateModal.as_view(), name='update-billing'),

    # Fee Table
    path('fee/table/', datatableviews.fee_table, name='admin-fee-table'),
    path('delete/fee/<int:pk>',
         modalviews.FeeDeleteModal.as_view(), name='delete-fee'),
    path('update/fee/<int:pk>',
         modalviews.FeeUpdateModal.as_view(), name='update-fee'),
    path('create/fee', modalviews.FeeCreateModal.as_view(), name='create-fee'),

    # Rental Table
    path('rental/table', datatableviews.rental_table, name='admin-rental-table'),
    path('read/rental/<int:pk>',
         modalviews.RentalReadModal.as_view(), name='read-rental'),
    path('delete/rental/<int:pk>',
         modalviews.RentalDeleteModal.as_view(), name='delete-rental'),
    path('update/rental/<int:pk>',
         modalviews.RentalUpdateModal.as_view(), name='update-rental'),

    # Tenant Table
    path('tenant/table', datatableviews.tenant_table, name='admin-tenant-table'),
    path('read/tenant/<int:pk>',
         modalviews.TenantReadModal.as_view(), name='read-tenant'),
]

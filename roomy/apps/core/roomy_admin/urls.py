from django.urls import path, include
from django.conf.urls.static import static
from .views import base, dashboard, cashflow, management, datatableviews, modalviews, reports
urlpatterns = [
    #     path('', base.index, name='admin-index'),
    path('logout/', base.admin_logout, name='admin-logout'),
    path('demo/<str:place>', base.demo, name='demo'),

    # dashboard
    path('',      dashboard.home,    name='admin-index'),
    path('home-ajax', dashboard.home_ajax, name='home-ajax'),
    path('dashboard/booking', dashboard.booking, name='booking'),
    path('dashboard/rental',      dashboard.rental,    name='rental'),
    path('dashboard/tenant',      dashboard.tenant,    name='tenant'),
    path('dashboard/notification',    dashboard.notif,    name='notif'),
    path('dashboard/request',  dashboard.tenant_request, name='request'),
    path('dashboard/guest',    dashboard.guest, name='guest'),

    # cashflow
    path('cashflow/expense',      cashflow.expense,  name='expense'),
    path('cashflow/billing',      cashflow.billing,  name='billing'),
    path('cashflow/fee',      cashflow.fee, name='fee'),

    # management
    path('management/property',      management.property_management,
         name='property_management'),
    path('management/catalog',      management.catalog_management,
         name='catalog_management'),
    path('management/room',      management.room_management, name='room_management'),
    #     path('management/account',      management.admin_management,
    #          name='admin_management'),
    path('management/owner-notifs', management.owner_notification,
         name='owner_notification'),
    path('management/owner-profile',
         management.owner_profile, name='owner-profile'),

    # Data Table Paths
    # Billing Table
    path('billing/table/<int:pk>', datatableviews.billing_table,
         name='admin-billing-table'),
    path('read/billing/<int:pk>',
         modalviews.BillingReadModal.as_view(), name='read-billing'),
    path('delete/billing/<int:pk>',
         modalviews.BillingDeleteModal.as_view(), name='delete-billing'),
    path('update/billing/<int:pk>',
         modalviews.BillingUpdateModal.as_view(), name='update-billing'),

    # Fee Table
    path('fee/table/<int:pk>', datatableviews.fee_table, name='admin-fee-table'),
    path('delete/fee/<int:pk>',
         modalviews.FeeDeleteModal.as_view(), name='delete-fee'),
    path('update/fee/<int:pk>',
         modalviews.FeeUpdateModal.as_view(), name='update-fee'),
    path('create/fee/<int:pk>', modalviews.FeeCreateModal, name='create-fee'),

    # Rental Table
    path('manage-tenants/<int:pk>', modalviews.ManageTenantsModal,
         name='admin-manage-tenants'),
    path('remove-tenant/<int:pk>/<int:idk>',
         modalviews.RemoveTenantModal, name='admin-remove-tenant'),
    path('rental/table/<int:pk>', datatableviews.rental_table,
         name='admin-rental-table'),
    path('read/rental/<int:pk>',
         modalviews.RentalReadModal.as_view(), name='read-rental'),
    path('delete/rental/<int:pk>',
         modalviews.RentalDeleteModal.as_view(), name='delete-rental'),
    path('update/rental/<int:pk>',
         modalviews.RentalUpdateModal.as_view(), name='update-rental'),

    # Tenant Table
    path('add/tenant/<int:pk>', modalviews.AddTenantModal, name='admin-add-tenant'),
    path('tenant/table/<int:pk>', datatableviews.tenant_table,
         name='admin-tenant-table'),
    path('read/tenant/<int:pk>',
         modalviews.TenantReadModal.as_view(), name='read-tenant'),

    # Expense Table
    path('expense/table/<int:pk>', datatableviews.expense_table,
         name='admin-expense-table'),
    path('create/expense/<int:pk>', modalviews.ExpenseCreateModal,
         name='create-expense'),
    path('delete/expense/<int:pk>',
         modalviews.ExpenseDeleteModal.as_view(), name='delete-expense'),
    path('update/expense/<int:pk>',
         modalviews.ExpenseUpdateModal.as_view(), name='update-expense'),

    # Guest Table
    path('guest/table/<int:pk>', datatableviews.guest_table,
         name='admin-guest-table'),
    path('create/guest', modalviews.GuestCreateModal.as_view(), name='create-guest'),
    path('delete/guest/<int:pk>',
         modalviews.GuestDeleteModal.as_view(), name='delete-guest'),
    path('update/guest/<int:pk>',
         modalviews.GuestUpdateModal.as_view(), name='update-guest'),

    # Tenant Request
    path('request/table/<int:pk>', datatableviews.request_table,
         name='admin-request-table'),
    path('delete/request/<int:pk>',
         modalviews.RequestDeleteModal.as_view(), name='delete-request'),
    path('update/request/<int:pk>',
         modalviews.RequestUpdateModal.as_view(), name='update-request'),

    # Tenant Notifs
    path('notif/table/', datatableviews.notif_table, name='admin-notif-table'),
    path('delete/notif/<int:pk>',
         modalviews.NotifDeleteModal.as_view(), name='delete-notif'),
    path('update/notif/<int:pk>',
         modalviews.NotifUpdateModal.as_view(), name='update-notif'),
    path('create/notif', modalviews.NotifCreateModal.as_view(), name='create-notif'),

    # Booking
    path('booking/table/<int:pk>', datatableviews.booking_table,
         name='admin-booking-table'),
    path('read/booking/<int:pk>',
         modalviews.BookingReadModal.as_view(), name='read-booking'),
    path('delete/booking/<int:pk>',
         modalviews.BookingDeleteModal.as_view(), name='delete-booking'),
    path('update/booking/<int:pk>',
         modalviews.BookingUpdateModal.as_view(), name='update-booking'),

    # Property
    path('property/table/', datatableviews.property_table,
         name='admin-property-table'),
    path('read/property/<int:pk>',
         modalviews.PropertyReadModal.as_view(), name='read-property'),
    path('create/property', modalviews.PropertyCreateModal,
         name='create-property'),
    path('delete/property/<int:pk>',
         modalviews.PropertyDeleteModal.as_view(), name='delete-property'),
    path('up/property/<int:pk>',
         modalviews.PropertyUpdateModal.as_view(), name='update-property'),
    path('upload/property/<int:pk>', base.property_upload,
         name='admin-property-upload'),

    # Catalog
    path('catalog/table/<int:pk>', datatableviews.catalog_table,
         name='admin-catalog-table'),
    path('create/catalog/<int:pk>',
         modalviews.CatalogCreateModal, name='create-catalog'),
    path('read/catalog/<int:pk>',
         modalviews.CatalogReadModal.as_view(), name='read-catalog'),
    path('delete/catalog/<int:pk>',
         modalviews.CatalogDeleteModal.as_view(), name='delete-catalog'),
    path('update/catalog/<int:pk>',
         modalviews.CatalogUpdateModal.as_view(), name='update-catalog'),
    path('upload/catalog2d/<int:pk>', base.catalog_upload2d,
         name='admin-catalog2d-upload'),
    path('upload/catalog3d/<int:pk>', base.catalog_upload3d,
         name='admin-catalog3d-upload'),

    # Room
    path('room/table/<int:pk>', datatableviews.room_table, name='admin-room-table'),
    path('create/room/<int:pk>', modalviews.RoomCreateModal, name='create-room'),
    path('read/room/<int:pk>',
         modalviews.RoomReadModal.as_view(), name='read-room'),
    path('delete/room/<int:pk>',
         modalviews.RoomDeleteModal.as_view(), name='delete-room'),
    path('update/room/<int:pk>',
         modalviews.RoomUpdateModal.as_view(), name='update-room'),

    # Owner Notifs
    path('onotif/table', datatableviews.onotif_table, name='owner-notif-table'),
    path('update/onotif/<int:pk>',
         modalviews.OnotifUpdateModal.as_view(), name='update-onotif'),
    path('read/onotif/<int:pk>',
         modalviews.OnotifReadModal.as_view(), name='read-onotif'),

    # Account
    #     path('account_management/table/',
    #          datatableviews.admin_acc_table,  name='admin-acc-table'),
    #     path('read/admin_acc/<int:pk>', modalviews.AdminAccReadModal.as_view(),
    #          name='read-admin-acc'),
    #     path('delete/admin_acc/<int:pk>',
    #          modalviews.AdminAccDeleteModal.as_view(), name='delete-admin-acc'),
    #     path('update/admin_acc/<int:pk>',
    #          modalviews.AdminAccUpdateModal.as_view(), name='update-admin-acc'),

    # Generate reports
     path('generate-report', reports.generate_report, name='generate-report'),

    path('generate/properties', reports.list_properties, name='list-properties'),
    path('generate/rooms/<int:pk>', reports.list_rooms, name='list-rooms'),
    path('generate/tenants/<int:pk>', reports.list_tenants, name='list-tenants'),
    path('generate/payments/<int:pk>', reports.list_payments, name='list-payments'),
    path('generate/expenses/<int:pk>', reports.list_expenses, name='list-expenses'),
    path('generate/cashflow/<str:date>', reports.generate_my_cashflow, name='generate-my-cashflow'),

]

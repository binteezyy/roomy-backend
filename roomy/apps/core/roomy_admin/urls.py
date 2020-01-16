from django.urls import path, include
from django.conf.urls.static import static
from .views import base, datatableviews, modalviews
urlpatterns = [
    path('', base.index, name='admin-index'),
    path('logout/', base.admin_logout, name='admin-logout'),


    path('demo/<str:place>', base.demo, name='demo'),
    path('dashboard/',      base.dashboard,
         name='dashboard'),
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
    path('guest/', base.guest, name='guest'),
    path('request/', base.tenant_request, name='request'),
    path('notif/', base.notif, name='notif'),
    path('booking/', base.booking, name='booking'),

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

    # Expense Table
    path('expense/table', datatableviews.expense_table,
         name='admin-expense-table'),
    path('create/expense', modalviews.ExpenseCreateModal.as_view(),
         name='create-expense'),
    path('delete/expense/<int:pk>',
         modalviews.ExpenseDeleteModal.as_view(), name='delete-expense'),
    path('update/expense/<int:pk>',
         modalviews.ExpenseUpdateModal.as_view(), name='update-expense'),

    # Guest Table
    path('guest/table', datatableviews.guest_table, name='admin-guest-table'),
    path('create/guest', modalviews.GuestCreateModal.as_view(), name='create-guest'),
    path('delete/guest/<int:pk>',
         modalviews.GuestDeleteModal.as_view(), name='delete-guest'),
    path('update/guest/<int:pk>',
         modalviews.GuestUpdateModal.as_view(), name='update-guest'),

    # Tenant Request
    path('request/table', datatableviews.request_table,
         name='admin-request-table'),
    path('delete/request/<int:pk>',
         modalviews.RequestDeleteModal.as_view(), name='delete-request'),
    path('update/request/<int:pk>',
         modalviews.RequestUpdateModal.as_view(), name='update-request'),

    # Tenant Notifs
    path('notif/table', datatableviews.notif_table, name='admin-notif-table'),
    path('delete/notif/<int:pk>',
         modalviews.NotifDeleteModal.as_view(), name='delete-notif'),
    path('update/notif/<int:pk>',
         modalviews.NotifUpdateModal.as_view(), name='update-notif'),
    path('create/notif', modalviews.NotifCreateModal.as_view(), name='create-notif'),

    # Booking
    path('booking/table', datatableviews.booking_table,
         name='admin-booking-table'),
    path('read/booking/<int:pk>',
         modalviews.BookingReadModal.as_view(), name='read-booking'),
    path('delete/booking/<int:pk>',
         modalviews.BookingDeleteModal.as_view(), name='delete-booking'),
    path('update/booking/<int:pk>',
         modalviews.BookingUpdateModal.as_view(), name='update-booking'),

    # Property
    path('property/table', datatableviews.property_table,
         name='admin-property-table'),
    path('create/property', modalviews.PropertyCreateModal.as_view(),
         name='create-property'),
    path('delete/property/<int:pk>',
         modalviews.PropertyDeleteModal.as_view(), name='delete-property'),
    path('update/property/<int:pk>',
         modalviews.PropertyUpdateModal.as_view(), name='update-property'),
    path('upload/property', base.property_upload, name='admin-property-upload'),

    # Room
    path('room/table', datatableviews.room_table, name='admin-room-table'),
    path('create/room', modalviews.RoomCreateModal.as_view(), name='create-room'),
    path('delete/room/<int:pk>',
         modalviews.RoomDeleteModal.as_view(), name='delete-room'),
    path('update/room/<int:pk>',
         modalviews.RoomUpdateModal.as_view(), name='update-room'),
    path('upload/room2d', base.room_upload2d, name='admin-room2d-upload'),
    path('upload/room3d', base.room_upload3d, name='admin-room3d-upload'),

    # Admin Accounts
    path('admin_management/table',
         datatableviews.admin_acc_table,  name='admin-acc-table'),
    path('read/admin_acc/<int:pk>', modalviews.AdminAccReadModal.as_view(),
         name='read-admin-acc'),
    path('delete/admin_acc/<int:pk>',
         modalviews.AdminAccDeleteModal.as_view(), name='delete-admin-acc'),
    path('update/admin_acc/<int:pk>',
         modalviews.AdminAccUpdateModal.as_view(), name='update-admin-acc'),
]

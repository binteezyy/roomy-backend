from django.urls import path,include
from ..views import *
from ..views.session import session_urls
from .notification import notification_urls
from ..tables import *
urlpatterns = [
    #navigation
    path('modals/', include('apps.client.urls.modals')),
    path('notifications/', include(notification_urls)),
    path('sessions/', include(session_urls)),
    path('', landing.home, name='home'),
    path('login/',auth.clogin, name='login'),
    path('logout/', auth.clogout, name='logout'),
    path('sign-up/',auth.csign_up, name='sign_up'),
    path('forgot-password/', auth.cforgot_password, name='forgot_password'),
    path('explore/', explore.index, name='explore'),
    path('partner_with_us/', landing.partner_with_us, name='partner_with_us'),
    path('partner_with_us/application/',auth.get_in_touch, name='get_in_touch'),
    path('partner-with-us/application/submit/',auth.owner_application_submit, name="partner-submit"),
    path('about/', landing.about, name='about'),
    path('faq/', landing.faq, name='faq'),
    path('contact/', landing.contact, name='contact'),
    path('terms_of_use/', landing.terms_of_use, name='terms_of_use'),
    path('privacy_policy/', landing.privacy, name='privacy'),
    path('authListener/', auth.authListener, name='authListener'),
    path('404/', landing.page_not_found, name='page_not_found'),

    #property
    path('explore/', explore.index, name='explore'),
    path('explore/property/', property.property, name='property'),
    path('explore/property/room/<int:pk>', explore.room_view, name='room'),
    path('explore/property/room/<int:pk>/book', transaction.booking_modal, name='booking-confirm'),
    path('explore/property/amenities', property.amenities, name='amenities'),
    path('explore/property/photos', property.photos, name='photos'),
    path('explore/property/room/booking', property.booking, name='booking'),

    ## ACCOUNT
    path('account/bookings', account.bookings, name='bookings'),
    path('account/bookings/<int:pk>', account.BookingView, name='booking-view'),
    # ACCOUNT - REQUEST
    path('account/bookings/<int:pk>/request/create', account.BookingRequest, name='booking-request'),
    path('account/bookings/<int:pk>/request/', account.BookingRequestList, name='booking-request-list'),
    path('account/bookings/<int:pk>/request/table', RequestsTable, name='booking-request-table'),
    # ACCOUNT - BILLING
    path('account/bookings/<int:pk>/billing/', account.BookingBillingList, name='booking-billing-list'),
    path('account/bookings/<int:pk>/billing/table', BillingsTable, name='booking-billing-table'),
    # ACCOUNT - ETC
    path('account/saved', account.saved, name='saved'),
    path('account/messages', account.messages, name='messages'),
    path('account/profile', account.profile, name='profile'),
]

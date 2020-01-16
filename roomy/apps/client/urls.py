from django.urls import path,include
from django.conf.urls.static import static
from .views import landing
from .views import property

urlpatterns = [
    #navigation
    path('', landing.home, name='home'),
    path('explore/', landing.explore, name='explore'),
    path('booking_guide/', landing.booking_guide, name='booking_guide'),
    path('partner_with_us/', landing.partner_with_us, name='partner_with_us'),
    path('about/', landing.about, name='about'),
    path('faq/', landing.faq, name='faq'),
    path('contact/', landing.contact, name='contact'),
    path('terms_of_use/', landing.terms_of_use, name='terms_of_use'),
    path('privacy/', landing.privacy, name='privacy'),
    path('help_center/', landing.help_center, name='help_center'),
    #property
    path('explore/property/room', property.room, name='room'),
    path('explore/property/amenities', property.amenities, name='amenities'),
    path('explore/property/photos', property.photos, name='photos'),
    path('explore/property/rates', property.rates, name='rates'),
]

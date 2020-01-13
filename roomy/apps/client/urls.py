from django.urls import path,include
from django.conf.urls.static import static
from .views import landing_pages
from .views import property

urlpatterns = [
    #navigation
    path('home/', landing_pages.home, name='home'),
    path('explore/', landing_pages.explore, name='explore'),
    path('how_to_book/', landing_pages.how_to_book, name='how_to_book'),
    path('partner_with_us/', landing_pages.partner_with_us, name='partner_with_us'),
    path('about/', landing_pages.about, name='about'),
    path('faq/', landing_pages.faq, name='faq'),
    path('contact/', landing_pages.contact, name='contact'),
    path('terms_of_use/', landing_pages.terms_of_use, name='terms_of_use'),
    path('privacy/', landing_pages.privacy, name='privacy'),
    path('help_center/', landing_pages.help_center, name='help_center'),
    #property
    path('explore/property/rooms', property.rooms, name='rooms'),
    path('explore/property/amenities', property.amenities, name='amenities'),
    path('explore/property/photos', property.photos, name='photos'),
]

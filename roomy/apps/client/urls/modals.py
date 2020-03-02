from django.urls import path,include
from ..views import auth
urlpatterns = [
    path('login/',auth.modal_auth, name='modal-login'),
]

from django.urls import path,include
from django.http                        import HttpResponse
import json
def session_clear_form(request):
    if request.session['form_error']: request.session.pop('form_error')
    return HttpResponse({'success': "Success"}, content_type="application/json")

session_urls = [
    path('session/clear-form', session_clear_form, name='clear-form'),
]

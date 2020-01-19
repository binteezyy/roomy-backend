from django.contrib import admin
from config.common import ClientAdmin
from django.apps import apps
from .models import *
models = apps.get_models()
excepts = ['Permission','Group','User','LogEntry','ContentType','Session',]

from pprint import pprint
import os

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]

        super(ListAdminMixin, self).__init__(model, admin_site)
# #
for model in models:
    print("MODEL:",model,type(model))
    if model.__name__ not in excepts:
        # if [True for x in inspect.getmro(model) if x.__name__=='SingletonModel']: # SIGLE OBJECT HANDLER

        admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass

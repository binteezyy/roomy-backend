from django.contrib import admin
from config.common import ClientAdmin
from django.apps import apps
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget
from .models import *
models = apps.get_models()
excepts = ['Permission','Group','User','LogEntry','ContentType','Session',]

from pprint import pprint
import os

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        formfield_overrides = {
            fields.JSONField: {'widget': JSONEditorWidget},
        }
        self.list_display = []
        for field in model._meta.fields:
            if field.name != "id":
                self.list_display.append(field.name)

        super(ListAdminMixin, self).__init__(model, admin_site)

def clean_admin_class(self,model):
    ## TODO: 
    return self
for model in models:
    if model.__name__ not in excepts:
        # if [True for x in inspect.getmro(model) if x.__name__=='SingletonModel']: # SIGLE OBJECT HANDLER

        admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
        admin_class = clean_admin_class(admin_class,model)
        try:
            admin.site.register(model,admin_class)
        except admin.sites.AlreadyRegistered:
            pass

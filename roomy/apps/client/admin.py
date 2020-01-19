from django.contrib import admin
from django.apps import apps
from .models import *
from ..commons.apps import strip_m2m

models = apps.get_models()
excepts = ['Permission','Group','User','LogEntry','ContentType','Session']

class TabularMixin(object):
    def __init__(self, model, admin_site):
        print(model)

        super(TabularMixin, self).__init__(model, admin_site)

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]

        # INLINE HANDLER
        # inlines = strip_m2m(model)
        # self.inlines = []
        # if inlines:
        #      for i in inlines:
        #          # self.inlines = [i.__name__ for i in inlines]
        #         inline_class = type(f'{i.__name__}Inline', (TabularMixin, admin.TabularInline), {})
        #         inline_class.model = i
        #         self.inlines += [inline_class]

        super(ListAdminMixin, self).__init__(model, admin_site)

for model in models:
    if model.__name__ not in excepts:
        # if [True for x in inspect.getmro(model) if x.__name__=='SingletonModel']: # SIGLE OBJECT HANDLER

        admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
        try:
            admin.site.register(model, admin_class)
        except admin.sites.AlreadyRegistered:
            pass

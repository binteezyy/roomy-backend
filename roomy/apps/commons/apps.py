from pprint import pprint
def get_model_type():
    pass
def strip_m2m(obj):
    from django.db.models.fields.related import ManyToManyField
    model_map = obj._meta.get_fields()
    x = list(map(lambda m: isinstance(m,ManyToManyField),[ i for i in model_map]))
    if True in x:
        return [y.related_model for i,y in enumerate(model_map) if x[i]]
    else:
        False

from django import template

register = template.Library()

@register.filter
def num_to_ordinal(value):
    import math
    ordinal = "%d%s" % (value,"tsnrhtdd"[(math.floor(value/10)%10!=1)*(value%10<4)*value%10::4])
    return ordinal

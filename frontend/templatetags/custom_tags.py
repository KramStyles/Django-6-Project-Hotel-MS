from django import template

register = template.Library()


@register.filter
def mod_pics(data):
    if data >= 7:
        data = (data % 7) + 1
    return data

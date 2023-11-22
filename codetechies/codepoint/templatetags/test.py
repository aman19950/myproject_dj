from django import template

register = template.Library()



@register.filter(name="cut")
def cut():
    return 1

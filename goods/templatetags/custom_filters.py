from django import template

register = template.Library()


@register.filter
def my_custom_filter(value):
    return value.upper()

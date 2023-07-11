from django import template

register = template.Library()


@register.filter
def get_initials(value):
    return "".join([word[:1].upper() for word in value.split(" ")])

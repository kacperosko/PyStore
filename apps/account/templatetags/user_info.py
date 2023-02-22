from django import template
from apps.authentication.models import User


register = template.Library()


def get_first_name(user):
    return user.first_name


register.filter('get_first_name', get_first_name)

from django import template
import os

register = template.Library()

@register.filter
def file_exists(value):
    return os.path.exists(value)
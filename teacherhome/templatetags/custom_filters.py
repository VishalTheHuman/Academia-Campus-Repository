from django import template

register = template.Library()

@register.filter(name='get_file_name')
def get_file_name(value):
    return value.split('/')[-1]
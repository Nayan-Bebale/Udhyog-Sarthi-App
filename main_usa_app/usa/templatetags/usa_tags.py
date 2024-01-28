# usa_tags.py

from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def signout_url():
    return reverse('usa:signout')

from django import template
from poison.models import *

register = template.Library()


@register.simple_tag(name='get_cats_news')
def get_categories_news():
    return CategoryNews.objects.all()


@register.simple_tag(name='get_albums')
def get_albums():
    return Album.objects.all()
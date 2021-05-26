from django.db.models import Count

from .models import *

menu = [{'title': 'news', 'url_name': 'news'},
        {'title': 'media', 'url_name': 'media'},
        {'title': 'tours', 'url_name': 'tours'},
        {'title': 'connect', 'url_name': 'connect'},
        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = CategoryNews.objects.annotate(Count('news'))  # кол-во записей в категории
        albums = Album.objects.all().annotate(Count('photo'))  # кол-во фото в альбомах
        photos = Photo.objects.all()  # все фото во всех альбомах
        tours = Tour.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        context['albums'] = albums
        context['photos'] = photos
        context['tours'] = tours
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
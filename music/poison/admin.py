from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_image',)
    save_on_top = True

    def get_image(self, obj):   # вывод изображения
        return mark_safe(f'<img src={obj.photo.url} width="70" height="60"')

    get_image.short_description = 'Изображение'


class CategoryNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_image',)
    save_on_top = True

    def get_image(self, obj):   # вывод изображения оболожки в админке
        return mark_safe(f'<img src={obj.image.url} width="70" height="60"')

    get_image.short_description = 'Обложка'


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'get_image')
    list_display_links = ('id', 'album')
    readonly_fields = ('get_image',)

    def get_image(self, obj):   # вывод изображения
        return mark_safe(f'<img src={obj.photo.url} width="70" height="60"')

    get_image.short_description = 'Фото'


class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'group_name', 'location', 'venue', 'tickets')
    list_display_links = ('id', 'date')
    search_fields = ('group_name',)
    save_on_top = True


admin.site.register(News, NewsAdmin)
admin.site.register(CategoryNews, CategoryNewsAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tour, TourAdmin)

admin.site.site_title = 'Admin panel Poison'
admin.site.site_header = 'Admin panel Poison'



from django.db import models
from django.urls import reverse


# Модель списка новостей
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст новости')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('CategoryNews', on_delete=models.PROTECT, null=True, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-time_create', 'title']


# Модель с категориями новостей
class CategoryNews(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category News')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name_plural = 'News Category'
        ordering = ['id']


# Модель альбома с фотографиями
class Album(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название Альбома')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL Альбома')
    image = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Обложка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery', kwargs={'album_slug': self.slug})

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ['title']


# Модель фото для альбома
class Photo(models.Model):
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото')
    album = models.ForeignKey(Album, on_delete=models.PROTECT, null=True, verbose_name='Альбом')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


# Модель туров групп
class Tour(models.Model):
    date = models.DateField(verbose_name='Дата проведения')
    group_name = models.CharField(max_length=50, verbose_name='Группа')
    location = models.CharField(max_length=50, verbose_name='Расположение')
    venue = models.CharField(max_length=100, verbose_name='Место')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    tickets = models.BooleanField(null=True, verbose_name='Билеты')

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name_plural = 'Tours'
        ordering = ['date']
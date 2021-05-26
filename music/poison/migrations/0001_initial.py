# Generated by Django 3.2.2 on 2021-05-19 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Category News')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'News Category',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата проведения')),
                ('group_name', models.CharField(max_length=50, verbose_name='Группа')),
                ('location', models.CharField(max_length=50, verbose_name='Расположение')),
                ('venue', models.CharField(max_length=100, verbose_name='Место')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('tickets', models.BooleanField(null=True, verbose_name='Билеты')),
            ],
            options={
                'verbose_name_plural': 'Tours',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Текст новости')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='poison.categorynews', verbose_name='Категории')),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['-time_create', 'title'],
            },
        ),
    ]
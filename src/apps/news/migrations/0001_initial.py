# Generated by Django 4.0.6 on 2024-04-16 17:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(
                    upload_to='photo_news', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Картинки Новостей',
                'verbose_name_plural': 'Картинки Новостей',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(
                    max_length=255, verbose_name='Название рубрики')),
                ('title_ru', models.CharField(max_length=255,
                 null=True, verbose_name='Название рубрики')),
                ('title_en', models.CharField(max_length=255,
                 null=True, verbose_name='Название рубрики')),
                ('title_ky', models.CharField(max_length=255,
                 null=True, verbose_name='Название рубрики')),
            ],
            options={
                'verbose_name': 'Рубрика новостей',
                'verbose_name_plural': 'Рубрики новостей',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, editable=False,
                 max_length=255, unique=True, verbose_name='URL представление')),
                ('title', models.CharField(blank=True,
                 max_length=255, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(blank=True,
                 max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(blank=True,
                 max_length=255, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(blank=True,
                 max_length=255, null=True, verbose_name='Название')),
                ('main_description', models.TextField(
                    blank=True, null=True, verbose_name='Main Описание')),
                ('main_description_ru', models.TextField(
                    blank=True, null=True, verbose_name='Main Описание')),
                ('main_description_en', models.TextField(
                    blank=True, null=True, verbose_name='Main Описание')),
                ('main_description_ky', models.TextField(
                    blank=True, null=True, verbose_name='Main Описание')),
                ('description', ckeditor.fields.RichTextField(
                    blank=True, null=True, verbose_name='Описание')),
                ('description_ru', ckeditor.fields.RichTextField(
                    blank=True, null=True, verbose_name='Описание')),
                ('description_en', ckeditor.fields.RichTextField(
                    blank=True, null=True, verbose_name='Описание')),
                ('description_ky', ckeditor.fields.RichTextField(
                    blank=True, null=True, verbose_name='Описание')),
                ('created', models.DateField(
                    default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('banner', models.ImageField(blank=True, null=True,
                 upload_to='photo_gallery', verbose_name='Изображение')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                 related_name='tags', to='news.newstag', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('-created',),
            },
        ),
    ]
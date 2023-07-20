from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone

from . import utils


class NewsTag(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название рубрики")

    class Meta:
        verbose_name = "Рубрика новостей"
        verbose_name_plural = "Рубрики новостей"
        ordering = ('-id',)

    def __str__(self):
        return self.title


@utils.autoslug("title")
class News(models.Model):
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        verbose_name="URL представление",
        editable=False,
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        blank=True, null=True,
    )
    main_descriotion = models.TextField(
        verbose_name="Main Описание",
        blank=True, null=True,
    )
    description = RichTextField(
        verbose_name="Описание",
        blank=True, null=True,
    )
    created = models.DateField(
        default=timezone.now, verbose_name="Дата создания")
    tag = models.ForeignKey(
        "NewsTag", verbose_name="Рубрика", on_delete=models.SET_NULL, null=True,
        related_name='tags'
    )
    banner = models.ImageField(
        upload_to="photo_gallery",
        verbose_name="Изображение",
        blank=True, null=True,
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('-created',)

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to="photo_news",
                              verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Картинки Новостей"
        verbose_name_plural = "Картинки Новостей"
        ordering = ('-id',)

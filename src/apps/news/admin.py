from django.conf import settings
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


@admin.register(models.News)
class NewsAdmin(TranslationAdmin):
    list_display = ('slug', 'title', 'created')


@admin.register(models.NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_image_url',
    )

    def get_image_url(self, obj):
        return f"{settings.BASE_URL}{obj.image.url}"


@admin.register(models.NewsTag)
class NewsTagAdmin(TranslationAdmin):
    list_display = ('title',)

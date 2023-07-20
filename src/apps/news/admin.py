from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


@admin.register(models.News)
class NewsAdmin(TranslationAdmin):
    list_display = ('slug', 'title', 'created')


@admin.register(models.NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.NewsTag)
class NewsTagAdmin(TranslationAdmin):
    list_display = ('title',)

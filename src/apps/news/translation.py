from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.News)
class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'main_description',)


@register(models.NewsTag)
class NewsTagTranslationOption(TranslationOptions):
    fields = ('title',)

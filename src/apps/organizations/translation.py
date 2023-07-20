from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Organization)
class OrganizationTranslationOption(TranslationOptions):
    fields = ('title', 'description')

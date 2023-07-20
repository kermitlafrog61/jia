from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Branch)
class GenreTranslationOption(TranslationOptions):
    fields = ('title', 'address',)


@register(models.TeamMember)
class TeamMemberTranslationOption(TranslationOptions):
    fields = ('fullname', 'position', 'description',)


@register(models.GoverningBody)
class GoverningBodyPrivilegesTranslationOption(TranslationOptions):
    fields = ('fullname', 'position', 'work_place', 'region',)


@register(models.Journal)
class JournalTranslationOption(TranslationOptions):
    fields = ('name',)


@register(models.Partnership)
class PartnershipTranslationOption(TranslationOptions):
    fields = ('description', 'memorandum', 'image')

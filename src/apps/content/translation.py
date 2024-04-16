from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.ActionPlane)
class ActionPlaneTranslationOption(TranslationOptions):
    fields = ('image',)


@register(models.FooterInfo)
class FooterInfoTranslationOption(TranslationOptions):
    fields = ('name',)


@register(models.BusinessSupport)
class BusinessSupportTranslationOption(TranslationOptions):
    fields = ('title',)


@register(models.MemberShipPrivileges)
class MemberShipPrivilegesTranslationOption(TranslationOptions):
    fields = ('title',)


@register(models.Contact)
class ContactPrivilegesTranslationOption(TranslationOptions):
    fields = ('title',)


@register(models.Report)
class ReportTranslationOption(TranslationOptions):
    fields = ('name', 'file')


@register(models.MainPageBanner)
class MainPageBannerTranslationOption(TranslationOptions):
    fields = ('title', 'description',)


@register(models.Situation)
class SituationTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'file', 'image')


@register(models.Organization)
class OrganizationTranslationOption(TranslationOptions):
    fields = ('title', 'description')


@register(models.ResidentJia)
class ResidentJiaTranslationOption(TranslationOptions):
    fields = ('file',)

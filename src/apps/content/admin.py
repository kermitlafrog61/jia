from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from . import models


class MemberShipPrivilegesAdmin(TranslationStackedInline):
    model = models.MemberShipPrivileges
    extra = 1


@admin.register(models.MemberShip)
class MemberShipAdmin(admin.ModelAdmin):
    inlines = [MemberShipPrivilegesAdmin]


@admin.register(models.Report)
class ReportAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(models.BusinessSupport)
class BusinessSupportAdmin(TranslationAdmin):
    list_display = (
        'title', 'created',
    )


@admin.register(models.MainPageBanner)
class MainPageBannerAdmin(TranslationAdmin):
    list_display = (
        'title', 'description')


class FooterPhoneAdmin(admin.StackedInline):
    model = models.FooterPhoneNumber
    extra = 1


class FooterEmailAdmin(admin.StackedInline):
    model = models.FooterEmail
    extra = 1


@admin.register(models.FooterInfo)
class FooterInfoAdmin(TranslationAdmin):
    list_display = ('name',)
    inlines = [FooterPhoneAdmin, FooterEmailAdmin]


@admin.register(models.ActionPlane)
class ActionPlaneAdmin(TranslationAdmin):
    list_display = ('image',)


@admin.register(models.Situation)
class SituationAdmin(TranslationAdmin):
    list_display = ('title', 'file',)


@admin.register(models.Organization)
class OrganizationAdmin(TranslationAdmin):
    list_display = ('title', 'category')


@admin.register(models.ResidentJia)
class ResidentJiaAdmin(TranslationAdmin):
    list_display = ('id',)


admin.site.register(models.Advertising)

admin.site.site_header = "JIA"
admin.site.site_title = "JIA ADMIN"
admin.site.index_title = "Добро пожаловать в JIA web-site Administration"

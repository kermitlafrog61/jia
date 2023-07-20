from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from decouple import config
from . import models

base_url = config('BASE_DOMAIN')


class MemberShipPrivilegesAdmin(TranslationStackedInline):
    model = models.MemberShipPrivileges
    extra = 1


@admin.register(models.MemberShip)
class MemberShipAdmin(admin.ModelAdmin):
    inlines = [MemberShipPrivilegesAdmin]


class ContactPhoneInline(admin.StackedInline):
    model = models.ContactPhone
    extra = 2


class ContactCellularInline(admin.StackedInline):
    model = models.ContactCellular
    extra = 2


class ContactEmailInline(admin.StackedInline):
    model = models.ContactEmail
    extra = 2


@admin.register(models.Contact)
class ContactAdmin(TranslationAdmin):
    inlines = [
        ContactPhoneInline,
        ContactCellularInline,
        ContactEmailInline,
    ]


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


admin.site.register(models.Event)
admin.site.register(models.Advertising)

admin.site.site_header = "JIA"
admin.site.site_title = "JIA ADMIN"
admin.site.index_title = "Добро пожаловать в JIA web-site Administration"

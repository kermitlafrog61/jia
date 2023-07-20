from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from . import models


@admin.register(models.GoverningBody)
class GoverningBodyAdmin(TranslationAdmin):
    list_display = (
        'fullname', 'position')


@admin.register(models.Branch)
class BranchAdmin(TranslationAdmin):
    list_display = ('title', 'mobile_number', 'work_number',
                    'address', 'email', 'place')


@admin.register(models.Partnership)
class PartnershipAdmin(TranslationAdmin):
    list_display = ('company_name', 'memorandum')


@admin.register(models.Journal)
class JournalAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(models.TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position')


@admin.site.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('title',)

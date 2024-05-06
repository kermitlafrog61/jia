from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


@admin.register(models.GoverningBody)
class GoverningBodyAdmin(TranslationAdmin):
    list_display = (
        'fullname', 'position')


class BranchPhoneInline(admin.StackedInline):
    model = models.BranchPhone
    extra = 2


class BranchCellularInline(admin.StackedInline):
    model = models.BranchCellular
    extra = 2


class BranchEmailInline(admin.StackedInline):
    model = models.BranchEmail
    extra = 2


@admin.register(models.Branch)
class BranchAdmin(TranslationAdmin):
    list_display = ('title', 'address', 'place')
    inlines = [
        BranchPhoneInline,
        BranchCellularInline,
        BranchEmailInline,
    ]


@admin.register(models.Partnership)
class PartnershipAdmin(TranslationAdmin):
    list_display = ('company_name', 'memorandum')


@admin.register(models.Journal)
class JournalAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(models.TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position')


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('title',)

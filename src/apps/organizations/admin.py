from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


@admin.register(models.Organization)
class OrganizationAdmin(TranslationAdmin):
    list_display = ('title', 'category')

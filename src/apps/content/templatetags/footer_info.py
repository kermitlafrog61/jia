from django import template

from .. import models

register = template.Library()


@register.simple_tag()
def get_footer_info():
    return models.FooterInfo.objects.all()

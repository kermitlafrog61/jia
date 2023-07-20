from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from transliterate import slugify as slugify_translit
from transliterate import detect_language

import random
import string


def random_string(size=5, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def autoslug(fieldname):
    def decorator(model):

        # Проверка полей модели
        assert hasattr(model, fieldname), f"Model has no field {fieldname!r}"
        assert hasattr(model, "slug"), "Model is missing a slug field"

        # Генерирует slug
        @receiver(models.signals.pre_save, sender=model, weak=False)
        def generate_slug(sender, instance, *args, raw=False, **kwargs):
            if not raw and not instance.slug:
                source = getattr(instance, fieldname)
                lang = detect_language(source)
                if lang:
                    slug = slugify_translit(source, lang)
                else:
                    slug = slugify(source, allow_unicode=True)

                Class = instance.__class__
                qs_exsists = Class.objects.filter(slug=slug).exists()

                if qs_exsists:
                    new_slug = "{slug}-{randstr}".format(
                        slug=slug, randstr=random_string(size=4)
                    )
                    instance.slug = new_slug
                else:
                    instance.slug = slug

        return model

    return decorator

from django.db import models
from ckeditor.fields import RichTextField


class Organization(models.Model):
    class Category(models.TextChoices):
        club = "CLUB", "Клуб"
        committee = "COMMITTEE", "Комитет"

    category = models.CharField(
        max_length=10,
        verbose_name="Категория",
        choices=Category.choices,
    )
    title = models.CharField(max_length=255, verbose_name="Имя организации")
    description = RichTextField(verbose_name="Информация об организации")
    image = models.ImageField(upload_to='organization/',
                              verbose_name='Картинка организации')
    icon = models.CharField(max_length=127, verbose_name="Иконка (https://remixicon.com)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

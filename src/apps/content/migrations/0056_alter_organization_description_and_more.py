# Generated by Django 4.0.6 on 2023-07-04 15:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0055_organization_icon_alter_organization_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Информация об организации'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Информация об организации'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Информация об организации'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Информация об организации'),
        ),
    ]
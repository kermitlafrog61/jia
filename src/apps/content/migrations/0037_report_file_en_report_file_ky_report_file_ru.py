# Generated by Django 4.0.6 on 2022-08-31 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0036_actionplane_image_en_actionplane_image_ky_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='file_en',
            field=models.FileField(null=True, upload_to='reports', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='report',
            name='file_ky',
            field=models.FileField(null=True, upload_to='reports', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='report',
            name='file_ru',
            field=models.FileField(null=True, upload_to='reports', verbose_name='Файл'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0028_remove_governingbody_image_remove_governingbody_main_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='governingbody',
            name='region_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='governingbody',
            name='region_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='governingbody',
            name='region_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Регион'),
        ),
    ]

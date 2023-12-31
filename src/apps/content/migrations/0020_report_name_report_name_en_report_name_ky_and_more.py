# Generated by Django 4.0.6 on 2022-07-08 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='report',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='report',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]

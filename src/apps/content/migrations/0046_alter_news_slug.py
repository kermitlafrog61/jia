# Generated by Django 4.0.6 on 2023-02-06 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0045_alter_news_banner_alter_news_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, unique=True, verbose_name='URL представление'),
        ),
    ]
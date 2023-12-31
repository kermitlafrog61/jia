# Generated by Django 4.0.6 on 2022-07-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0023_journal_name_en_journal_name_ky_journal_name_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='facebook',
            field=models.URLField(null=True, verbose_name='facebook'),
        ),
        migrations.AddField(
            model_name='news',
            name='instagram',
            field=models.URLField(null=True, verbose_name='instagram'),
        ),
        migrations.AddField(
            model_name='news',
            name='telegram',
            field=models.URLField(null=True, verbose_name='telegram'),
        ),
        migrations.AddField(
            model_name='news',
            name='twitter',
            field=models.URLField(null=True, verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='news',
            name='whatsapp',
            field=models.URLField(null=True, verbose_name='whatsapp'),
        ),
    ]

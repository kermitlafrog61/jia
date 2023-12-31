# Generated by Django 4.0.6 on 2023-07-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0053_remove_footerinfo_email_footeremail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CLUB', 'Клуб'), ('COMMITTEE', 'Комитет')], max_length=10, verbose_name='Категория')),
                ('title', models.CharField(max_length=255, verbose_name='Имя организации')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Имя организации')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Имя организации')),
                ('title_ky', models.CharField(max_length=255, null=True, verbose_name='Имя организации')),
                ('description', models.TextField(verbose_name='Информация об организации')),
                ('description_ru', models.TextField(null=True, verbose_name='Информация об организации')),
                ('description_en', models.TextField(null=True, verbose_name='Информация об организации')),
                ('description_ky', models.TextField(null=True, verbose_name='Информация об организации')),
                ('image', models.ImageField(upload_to='organization/', verbose_name='Локация орбиты')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
    ]

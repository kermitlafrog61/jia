# Generated by Django 4.0.6 on 2024-04-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentJia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file', verbose_name='PDF')),
                ('file_ru', models.FileField(null=True, upload_to='file', verbose_name='PDF')),
                ('file_en', models.FileField(null=True, upload_to='file', verbose_name='PDF')),
                ('file_ky', models.FileField(null=True, upload_to='file', verbose_name='PDF')),
            ],
            options={
                'verbose_name': 'Резиденты Jia',
                'verbose_name_plural': 'Резиденты Jia',
            },
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-15 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0031_remove_news_facebook_remove_news_instagram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='advertising', verbose_name='Изображение')),
                ('link', models.URLField(verbose_name='Ссылка на официальный рекламу')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламы',
            },
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('-date',), 'verbose_name': 'Отчет', 'verbose_name_plural': 'Отчеты'},
        ),
    ]
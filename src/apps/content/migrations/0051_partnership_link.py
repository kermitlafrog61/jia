# Generated by Django 4.0.6 on 2023-07-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0050_membership_district_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnership',
            name='link',
            field=models.URLField(default='https://jia.kg/', verbose_name='Ссылка на сайт'),
            preserve_default=False,
        ),
    ]

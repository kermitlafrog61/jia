# Generated by Django 4.0.5 on 2022-06-30 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_contact_contactphone_contactemail_contactcellular'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
    ]

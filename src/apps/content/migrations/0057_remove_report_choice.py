# Generated by Django 4.0.6 on 2023-07-04 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0056_alter_organization_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='choice',
        ),
    ]

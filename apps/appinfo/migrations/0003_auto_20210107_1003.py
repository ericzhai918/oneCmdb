# Generated by Django 3.0.7 on 2021-01-07 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicinfo', '0004_envlist'),
        ('appinfo', '0002_auto_20210107_0958'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SystemResourcesClass',
            new_name='SystemList',
        ),
    ]

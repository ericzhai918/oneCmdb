# Generated by Django 3.0.7 on 2021-01-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicinfo', '0003_auto_20210106_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env_name', models.CharField(max_length=64, unique=True, verbose_name='环境名称')),
            ],
            options={
                'verbose_name': '环境列表',
                'verbose_name_plural': '环境列表',
                'db_table': 'table_env_list',
            },
        ),
    ]

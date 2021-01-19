# Generated by Django 3.0.7 on 2021-01-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectGroupList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=64, unique=True, verbose_name='项目组名称')),
                ('group_owner', models.CharField(max_length=64, verbose_name='项目组负责人')),
            ],
            options={
                'verbose_name': '项目组列表',
                'verbose_name_plural': '项目组列表',
                'db_table': 'table_project_group',
            },
        ),
    ]

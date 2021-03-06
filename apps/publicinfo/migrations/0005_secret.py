# Generated by Django 3.0.7 on 2021-01-07 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicinfo', '0004_envlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ak', models.CharField(max_length=50, verbose_name='ak')),
                ('sk', models.CharField(max_length=50, verbose_name='sk')),
                ('user', models.CharField(max_length=50, verbose_name='ak用户')),
                ('firm_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicinfo.FirmList', verbose_name='厂商名称')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
                'db_table': 'secret',
            },
        ),
    ]

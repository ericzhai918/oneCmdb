# Generated by Django 3.0.7 on 2021-01-19 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0009_auto_20210119_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configdetails',
            name='app_short',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appinfo.SystemList', verbose_name='所属系统简称'),
        ),
        migrations.AlterField(
            model_name='configdetails',
            name='config_md5',
            field=models.CharField(max_length=64, unique=True, verbose_name='配置项MD5值'),
        ),
        migrations.AlterField(
            model_name='configdetails',
            name='config_path',
            field=models.CharField(max_length=256, verbose_name='配置文件路径'),
        ),
        migrations.AlterField(
            model_name='configdetails',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='IP地址'),
        ),
        migrations.AlterField(
            model_name='configdetails',
            name='lines',
            field=models.IntegerField(verbose_name='行号'),
        ),
        migrations.AlterField(
            model_name='configdetails',
            name='subapp_short',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appinfo.SubSystemList', verbose_name='所属子系统简称'),
        ),
    ]

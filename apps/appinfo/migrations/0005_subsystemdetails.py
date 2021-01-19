# Generated by Django 3.0.7 on 2021-01-08 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0004_subsystemlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSystemDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='IP地址')),
                ('app_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='应用类型')),
                ('logical_domain', models.CharField(blank=True, max_length=64, null=True, verbose_name='网络区域')),
                ('physical_domian', models.CharField(blank=True, max_length=64, null=True, verbose_name='物理区域')),
                ('start_user', models.CharField(blank=True, default='app', max_length=64, null=True, verbose_name='启动用户')),
                ('app_dir', models.CharField(blank=True, max_length=128, null=True, verbose_name='应用目录')),
                ('backup_dir', models.CharField(blank=True, max_length=128, null=True, verbose_name='备份目录')),
                ('app_path', models.CharField(blank=True, max_length=128, null=True, verbose_name='应用包名')),
                ('log_path', models.CharField(blank=True, max_length=128, null=True, verbose_name='应用日志目录')),
                ('config_path', models.CharField(blank=True, max_length=128, null=True, verbose_name='应用配置目录')),
                ('start_script', models.CharField(blank=True, max_length=128, null=True, verbose_name='启动脚本')),
                ('stop_scritp', models.CharField(blank=True, max_length=128, null=True, verbose_name='停止脚本')),
                ('version', models.CharField(blank=True, max_length=128, null=True, verbose_name='当前版本')),
                ('shared_dir', models.CharField(blank=True, max_length=128, null=True, verbose_name='共享存储目录')),
                ('port', models.CharField(blank=True, max_length=128, null=True, verbose_name='启动端口')),
                ('status', models.CharField(blank=True, max_length=128, null=True, verbose_name='服务状态')),
                ('app_short', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appinfo.SystemList', verbose_name='所属系统简称')),
                ('subapp_short', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appinfo.SubSystemList', verbose_name='所属子系统简称')),
            ],
            options={
                'verbose_name': '子系统资源清单',
                'verbose_name_plural': '子系统资源清单',
                'db_table': 'table_subapp_details',
                'ordering': ['id'],
                'unique_together': {('ip', 'subapp_short')},
            },
        ),
    ]

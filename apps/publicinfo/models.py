from django.db import models


# Create your models here.

class ProjectGroupList(models.Model):
    group_name = models.CharField(max_length=64, verbose_name='项目组名称', unique=True)
    group_owner = models.CharField(max_length=64, verbose_name='项目组负责人')

    class Meta:
        # django admin 管理界面的别名
        verbose_name = '项目组列表'
        verbose_name_plural = verbose_name
        # db_table 数据库中别名
        db_table = 'table_project_group'

    def __str__(self):
        return self.group_name


class FirmList(models.Model):
    firm_name = models.CharField(max_length=128, verbose_name='厂商名称', unique=True)
    firm_owner = models.CharField(max_length=128, verbose_name='厂商联系人')
    firm_phone = models.CharField(verbose_name="厂商联系电话", max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = '厂商列表'
        verbose_name_plural = verbose_name
        db_table = 'table_firm_list'

    def __str__(self):
        return self.firm_name


class EnvList(models.Model):
    env_name = models.CharField(max_length=64, verbose_name='环境名称', unique=True)

    class Meta:
        verbose_name = '环境列表'
        verbose_name_plural = verbose_name
        db_table = 'table_env_list'

    def __str__(self):
        return self.env_name

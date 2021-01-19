# -*- coding:utf-8 -*-
__author__ = 'Leon.Zhai'
__date__ = '2021/1/7 20:49'

from import_export import resources
from django.apps import apps

from appinfo.models import SystemList, SubSystemList, SubSystemDetails, DatabaseDetails, ConfigDetails
from publicinfo.models import ProjectGroupList, FirmList, EnvList


class BaseResource(resources.ModelResource):
    def __init__(self, appname, modelname):
        super().__init__()
        field_list = apps.get_model(appname, modelname)._meta.fields
        # field_list为 (<django.db.models.fields.AutoField: id>, <django.db.models.fields.CharField: group_name>, <django.db.models.fields.CharField: group_owner>)
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        # verbose_name_dict为{'id': 'ID', 'group_name': '项目组名称', 'group_owner': '项目组负责人'}

        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]


class ProjectGroupResource(BaseResource, resources.ModelResource):
    def __init__(self):
        super().__init__(appname='publicinfo', modelname='ProjectGroupList')

    class Meta:
        model = ProjectGroupList
        skip_unchanged = True
        # 导入数据时，如果该条数据没有修改，将会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过记录
        import_id_fields = ('id', 'group_name')
        # 对象标识的默认字段是ID，可以选择在导入时设置哪些字段用作id
        fileds = '__all__'


class FirmListResource(BaseResource, resources.ModelResource):
    def __init__(self):
        super().__init__(appname='publicinfo', modelname='FirmList')

    class Meta:
        model = FirmList
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id', 'firm_name')
        fileds = '__all__'


class EnvListResource(BaseResource, resources.ModelResource):
    def __init__(self):
        super().__init__(appname='publicinfo', modelname='EnvList')

    class Meta:
        model = EnvList
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id', 'env_name')
        fileds = '__all__'


class SystemListResource(BaseResource, resources.ModelResource):
    def __init__(self):
        super().__init__(appname='appinfo', modelname='SystemList')

    class Meta:
        model = SystemList
        skip_unchanged = True
        # 导入数据时，如果该条数据没有修改，将会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过记录
        import_id_fields = ('app_short',)
        # 对象标识的默认字段是ID，可以选择在导入时设置哪些字段用作id
        fileds = '__all__'


class SubSystemListResource(BaseResource, resources.ModelResource):
    def __init__(self):
        super().__init__(appname='appinfo', modelname='SubSystemList')

    class Meta:
        model = SubSystemList
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('subapp_short',)
        fileds = '__all__'


class SubSystemDetailsResource(BaseResource, resources.ModelResource):
    def __init__(self):
        super().__init__(appname='appinfo', modelname='SubSystemDetails')

    class Meta:
        model = SubSystemDetails
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('ip',)
        fileds = '__all__'


class DatabaseDetailsResource(BaseResource, resources.ModelResource):
    def __init__(self):
        super().__init__(appname='appinfo', modelname='DatabaseDetails')

    class Meta:
        model = DatabaseDetails
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('vip', 'vport')
        fileds = '__all__'


class ConfigDetailsResource(BaseResource, resources.ModelResource):
    def __init__(self):
        super().__init__(appname='appinfo', modelname='ConfigDetails')

    class Meta:
        model = ConfigDetails
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('ip', 'config_path')
        fileds = '__all__'

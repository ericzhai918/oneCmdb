from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from publicinfo.resource import SystemListResource, SubSystemListResource, SubSystemDetailsResource, \
    DatabaseDetailsResource, ConfigDetailsResource
from appinfo.models import SystemList, SubSystemList, SubSystemDetails, DatabaseDetails, ConfigDetails


# Register your models here.


@admin.register(SystemList)
class SystemAdmin(ImportExportModelAdmin):
    list_display = (
        'app_short', 'app_ch_full', 'dev_group', 'business_dept', 'pm', 'level', 'status', 'dev_mode', 'service_time',
        'firm_name')
    list_per_page = 20
    list_filter = ('app_short', 'app_ch_full', 'dev_group', 'level')
    list_display_links = ('app_short',)
    search_fields = ('app_short', 'business_dept', 'pm')
    show_detail_fields = ('app_short',)
    resource_class = SystemListResource


@admin.register(SubSystemList)
class SubSystemAdmin(ImportExportModelAdmin):
    list_display = (
        'subapp_short', 'subapp_ch_full', 'app_short', 'dev_a', 'dev_b', 'dev_owner', 'test_owner', 'ops_a', 'ops_b',
        'ops_owner', 'online_time')
    list_per_page = 20
    list_filter = ('subapp_short', 'subapp_ch_full')
    list_display_links = ('subapp_short',)
    search_fields = ('subapp_short',)
    show_detail_fields = ('subapp_short',)
    resource_class = SubSystemListResource


@admin.register(SubSystemDetails)
class SubSystemDetailsAdmin(ImportExportModelAdmin):
    list_display = (
        'ip', 'app_short', 'subapp_short', 'app_type', 'start_user', 'app_path', 'version', 'port', 'status',)
    list_per_page = 20
    list_filter = ('ip', 'app_short', 'subapp_short',)
    list_display_links = ('ip',)
    search_fields = ('ip', 'app_path',)
    show_detail_fields = ('ip',)
    resource_class = SubSystemDetailsResource


@admin.register(DatabaseDetails)
class DatabaseDetailsAdmin(ImportExportModelAdmin):
    list_display = (
        'vip', 'vport', 'setid', 'master_rip', 'master_rport', 'slave_rip', 'slave_rport', 'db_name', 'app_short',
        'subapp_short', 'dba_owner', 'dba_email', 'dba_phone')
    list_per_page = 20
    list_filter = ('vip', 'db_name', 'app_short', 'subapp_short')
    list_display_links = ('vip',)
    search_fields = ('vip', 'vport', 'setid', 'db_name')
    show_detail_fields = ('vip',)
    resource_class = DatabaseDetailsResource


@admin.register(ConfigDetails)
class ConfigDetailsAdmin(ImportExportModelAdmin):
    list_display = (
        'app_short', 'subapp_short', 'ip', 'config_path', 'lines', 'config_md5', 'old_conf', 'new_conf')
    list_per_page = 20
    list_filter = ('app_short', 'subapp_short', 'ip')
    list_display_links = ('app_short',)
    search_fields = ('config_path', 'old_conf')
    show_detail_fields = ('config_path',)
    resource_class = ConfigDetailsResource

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from publicinfo.models import ProjectGroupList, FirmList, EnvList
from publicinfo.resource import ProjectGroupResource, EnvListResource, FirmListResource


# Register your models here.


@admin.register(ProjectGroupList)
class ProjectGroupAdmin(ImportExportModelAdmin):
    # 显示的字段
    list_display = ('group_name', 'group_owner')
    list_per_page = 20
    # 筛选字段
    list_filter = ('id', 'group_name', 'group_owner')
    # 搜索字段
    search_fields = ('group_name', 'group_owner')
    ordering = ('group_name',)
    list_editable = ('group_owner',)
    # 可进入详情页字段
    list_display_links = ('group_name',)
    show_details_fields = ('group_name',)
    resource_class = ProjectGroupResource


# 在admin中注册绑定
# admin.site.register(ProjectGroupList, ProjectGroupAdmin)

@admin.register(FirmList)
class FirmListAdmin(ImportExportModelAdmin):
    # 显示的字段
    list_display = ('firm_name', 'firm_owner', 'firm_phone')
    list_per_page = 20
    # 筛选字段
    list_filter = ('id', 'firm_name', 'firm_owner')
    # 搜索字段
    search_fields = ('firm_name', 'firm_owner', 'firm_phone')
    ordering = ('firm_name',)
    list_editable = ('firm_owner', 'firm_phone')
    # 可进入详情页字段
    list_display_links = ('firm_name',)
    show_details_fields = ('firm_name',)
    resource_class = FirmListResource


@admin.register(EnvList)
class EnvListAdmin(ImportExportModelAdmin):
    list_display = ('env_name',)
    list_per_page = 20
    list_filter = ('env_name',)
    search_fields = ('env_name',)
    ordering = ('env_name',)
    list_display_links = ('env_name',)
    show_details_fields = ('env_name',)
    show_bookmarks = False
    resource_class = EnvListResource

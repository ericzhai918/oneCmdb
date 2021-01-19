from django.db import models
from publicinfo.models import ProjectGroupList, FirmList


# Create your models here.


class SystemList(models.Model):
    app_short = models.CharField(primary_key=True, max_length=128, verbose_name='系统简称')
    app_en_full = models.CharField(max_length=128, verbose_name='系统英文全称', blank=True, null=True)
    app_ch_full = models.CharField(max_length=128, verbose_name='系统中文全称', blank=True, null=True)
    app_explain = models.TextField(verbose_name='系统简介', blank=True, null=True)
    dev_group = models.ForeignKey(ProjectGroupList, on_delete=models.CASCADE, verbose_name='开发项目组', blank=True,
                                  null=True)
    business_dept = models.CharField(max_length=128, verbose_name='业务负责部门', blank=True, null=True)
    pm = models.CharField(max_length=128, verbose_name='产品经理', blank=True, null=True)
    level = models.CharField(max_length=8, verbose_name='系统等级', choices=(('A', 'A'), ('B', 'B'), ('C', 'C')),
                             blank=True, null=True)
    status = models.CharField(max_length=64, verbose_name='状态', blank=True, null=True)
    dev_mode = models.CharField(max_length=128, verbose_name='建设方式', blank=True, null=True)
    service_time = models.CharField(max_length=256, verbose_name='服务窗口', blank=True, null=True)
    firm_name = models.CharField(max_length=128, verbose_name='厂商名称', blank=True, null=True)

    class Meta:
        verbose_name = '应用系统清单'
        verbose_name_plural = verbose_name
        db_table = 'table_system_list'

    def __str__(self):
        return self.app_short


class SubSystemList(models.Model):
    subapp_short = models.CharField(primary_key=True, max_length=128, verbose_name='子系统简称')
    subapp_en_full = models.CharField(max_length=128, verbose_name='子系统英文全称', blank=True, null=True)
    subapp_ch_full = models.CharField(max_length=128, verbose_name='子系统中文全称', blank=True, null=True)
    app_short = models.ForeignKey(SystemList, on_delete=models.CASCADE, verbose_name='所属系统简称')
    subapp_id = models.IntegerField(verbose_name='子系统ID', blank=True, null=True)
    subapp_explain = models.TextField(verbose_name='子系统简介', blank=True, null=True)
    dev_a = models.CharField(max_length=128, verbose_name='开发A角', blank=True, null=True)
    dev_a_email = models.EmailField(verbose_name='开发A角邮箱', blank=True, null=True)
    dev_a_phone = models.CharField(verbose_name='开发A角电话', max_length=11, blank=True, null=True)
    dev_b = models.CharField(max_length=128, verbose_name='开发B角', blank=True, null=True)
    dev_b_email = models.EmailField(verbose_name='开发B角邮箱', blank=True, null=True)
    dev_b_phone = models.CharField(verbose_name='开发B角电话', max_length=11, blank=True, null=True)
    dev_owner = models.CharField(max_length=128, verbose_name='开发升级责任人', blank=True, null=True)
    test_owner = models.CharField(max_length=128, verbose_name='测试负责人', blank=True, null=True)
    ops_a = models.CharField(max_length=128, verbose_name='运维A角', blank=True, null=True)
    ops_a_email = models.EmailField(verbose_name='运维A角邮箱', blank=True, null=True)
    ops_a_phone = models.CharField(verbose_name='运维A角电话', max_length=11, blank=True, null=True)
    ops_b = models.CharField(max_length=128, verbose_name='运维B角', blank=True, null=True)
    ops_b_email = models.EmailField(verbose_name='运维B角邮箱', blank=True, null=True)
    ops_b_phone = models.CharField(verbose_name='运维B角电话', max_length=11, blank=True, null=True)
    ops_owner = models.CharField(max_length=128, verbose_name='运维升级责任人', blank=True, null=True)
    online_time = models.DateField(verbose_name='上线时间', blank=True, null=True)
    dev_language = models.CharField(max_length=128, verbose_name='开发语言', blank=True, null=True)
    frame = models.CharField(max_length=128, verbose_name='框架', blank=True, null=True)
    middleware = models.CharField(max_length=128, verbose_name='中间件产品', blank=True, null=True)
    deploy_location = models.IntegerField(verbose_name='部署位置', choices=((0, '行内'), (1, '行外')), blank=True, null=True)

    class Meta:
        verbose_name = '子系统清单'
        verbose_name_plural = verbose_name
        db_table = 'table_subsystem_list'

    def __str__(self):
        return self.subapp_short


class SubSystemDetails(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP地址')  # 带有检查 IP地址合法性的 CharField
    app_short = models.ForeignKey(SystemList, on_delete=models.CASCADE, verbose_name='所属系统简称')
    subapp_short = models.ForeignKey(SubSystemList, on_delete=models.CASCADE, verbose_name='所属子系统简称')
    app_type = models.CharField(max_length=64, verbose_name='应用类型', blank=True, null=True)
    logical_domain = models.CharField(max_length=64, verbose_name='网络区域', blank=True, null=True)
    physical_domian = models.CharField(max_length=64, verbose_name='物理区域', blank=True, null=True)
    start_user = models.CharField(max_length=64, default='app', verbose_name='启动用户', blank=True, null=True)
    app_dir = models.CharField(max_length=128, verbose_name='应用目录', blank=True, null=True)
    backup_dir = models.CharField(max_length=128, verbose_name='备份目录', blank=True, null=True)
    app_path = models.CharField(max_length=128, verbose_name='应用包名', blank=True, null=True)
    log_path = models.CharField(max_length=128, verbose_name='应用日志目录', blank=True, null=True)
    config_path = models.CharField(max_length=128, verbose_name='应用配置目录', blank=True, null=True)
    start_script = models.CharField(max_length=128, verbose_name='启动脚本', blank=True, null=True)
    stop_scritp = models.CharField(max_length=128, verbose_name='停止脚本', blank=True, null=True)
    version = models.CharField(max_length=128, verbose_name='当前版本', blank=True, null=True)
    shared_dir = models.CharField(max_length=128, verbose_name='共享存储目录', blank=True, null=True)
    port = models.CharField(max_length=128, verbose_name='启动端口', blank=True, null=True)
    status = models.CharField(max_length=128, verbose_name='服务状态', blank=True, null=True)

    class Meta:
        verbose_name = '子系统资源清单'
        verbose_name_plural = verbose_name
        # 联合唯一
        unique_together = (('ip', 'subapp_short'),)
        # 按照这个字段排序
        ordering = ['id', ]
        # 设置表名
        db_table = 'table_subsys_details'

    def __str__(self):
        return self.ip


class DatabaseDetails(models.Model):
    setid = models.CharField(max_length=128, verbose_name='所属set')
    vip = models.GenericIPAddressField(verbose_name='VIP')
    vport = models.IntegerField(verbose_name='TGW端口')
    master_rip = models.CharField(max_length=128, verbose_name='主节点IP')
    master_rport = models.CharField(max_length=128, verbose_name='主节点端口')
    slave_rip = models.CharField(max_length=128, verbose_name='备节点IP')
    slave_rport = models.CharField(max_length=128, verbose_name='备节点端口')
    db_name = models.CharField(max_length=128, verbose_name='数据库名称')
    app_short = models.ForeignKey(SystemList, on_delete=models.CASCADE, verbose_name='所属系统简称')
    subapp_short = models.ForeignKey(SubSystemList, on_delete=models.CASCADE, verbose_name='所属子系统简称')
    dba_owner = models.CharField(max_length=128, verbose_name='运维负责人', blank=True, null=True)
    dba_email = models.CharField(max_length=128, verbose_name='运维负责人邮箱', blank=True, null=True)
    dba_phone = models.CharField(max_length=128, verbose_name='运维负责人电话', blank=True, null=True)

    class Meta:
        verbose_name = '数据库资源详情'
        verbose_name_plural = verbose_name
        unique_together = (('vip', 'vport'),)
        db_table = 'table_db_details'

    def __str__(self):
        return self.db_name


class ConfigDetails(models.Model):
    # app_short = models.ForeignKey(SystemList, on_delete=models.CASCADE, verbose_name='所属系统简称',null=True)
    # subapp_short = models.ForeignKey(SubSystemList, on_delete=models.CASCADE, verbose_name='所属子系统简称',null=True)
    # ip = models.GenericIPAddressField(verbose_name='IP地址', blank=True, null=True)
    # config_path = models.CharField(max_length=256, verbose_name='配置文件路径', blank=True, null=True)
    # lines = models.IntegerField(verbose_name='行号', blank=True, null=True)
    # config_md5 = models.CharField(max_length=64, verbose_name='配置项MD5值', unique=True,null=True)
    # old_conf = models.TextField(verbose_name='旧配置', blank=True, null=True)
    # new_conf = models.TextField(verbose_name='新配置', blank=True, null=True)
    app_short = models.ForeignKey(SystemList, on_delete=models.CASCADE, verbose_name='所属系统简称',)
    subapp_short = models.ForeignKey(SubSystemList, on_delete=models.CASCADE, verbose_name='所属子系统简称')
    ip = models.GenericIPAddressField(verbose_name='IP地址',blank=False,null=False)
    config_path = models.CharField(max_length=256, verbose_name='配置文件路径',blank=False,null=False)
    lines = models.IntegerField(verbose_name='行号',blank=False,null=False)
    config_md5 = models.CharField(max_length=64, verbose_name='配置项MD5值', unique=True)
    old_conf = models.TextField(verbose_name='旧配置', blank=True, null=True)
    new_conf = models.TextField(verbose_name='新配置', blank=True, null=True)

    class Meta:
        verbose_name = '配置文件信息'
        verbose_name_plural = verbose_name
        db_table = 'table_config_details'

    def save(self, *args, **kwargs):
        import hashlib
        md5 = hashlib.md5()  # 获取一个md5加密算法对象
        md5value = str(self.config_path) + str(self.lines)
        md5.update(md5value.encode())  # 指定需要加密的字符串
        self.config_md5 = md5.hexdigest()
        super().save(*args, **kwargs)

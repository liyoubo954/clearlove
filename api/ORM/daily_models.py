from tortoise import fields
from tortoise.models import Model

class daily_paper(Model):
    id = fields.IntField(pk=True)
    areaId = fields.IntField(description="盾构机编码id", null=True)
    ljsh = fields.IntField(description="累积时间", null=True)
    dpnj = fields.CharField(max_length=255, description="刀盘扭矩", null=True)
    jjbz = fields.CharField(max_length=255, description="进尺比重", null=True)
    cjll = fields.CharField(max_length=255, description="出浆流量", null=True)
    dpzs = fields.CharField(max_length=255, description="刀盘转速", null=True)
    kslc = fields.IntField(description="开始里程", null=True)
    qjcd = fields.IntField(description="区间长度", null=True)
    tjsd = fields.CharField(max_length=255, description="推进速度", null=True)
    jjll = fields.CharField(max_length=255, description="进浆流量", null=True)
    cjbz = fields.CharField(max_length=255, description="出浆比重", null=True)
    jrjd = fields.CharField(max_length=255, description="今日进度环", null=True)
    ztl = fields.CharField(max_length=255, description="总推力", null=True)
    qjyl = fields.IntField(description="区间余量", null=True)
    grd = fields.CharField(max_length=255, description="贯入度", null=True)
    wcd = fields.CharField(max_length=255, description="完成度", null=True)
    qkyl = fields.CharField(max_length=255, description="初压力", null=True)
    qpcyl = fields.CharField(max_length=255, description="气泡仓压力", null=True)
    qjmc = fields.CharField(max_length=255, description="区间名称", null=True)
    dgjbh = fields.CharField(max_length=255, description="盾构机编号", null=True)
    pjrjc = fields.IntField(description="平均日进尺", null=True)
    jslc = fields.IntField(description="结束里程", null=True)
    sfsj = fields.CharField(max_length=255, description="始发时间", null=True)
    time = fields.DateField(description="日期", null=True)

    class Meta:
        table = "daily_paper"
        app = "ddg_models"
        default_connection = "ddg_tenant_conn"
# models/ddg_models/project_report.py

from tortoise.models import Model
from tortoise import fields

class bar_chart_report(Model):
    id = fields.IntField(pk=True)
    sub_code = fields.CharField(max_length=50, description="项目编码", null=True)
    sub_name = fields.CharField(max_length=100, description="项目名称", null=True)
    type = fields.IntField(description="类型标识", null=True)
    connect_key = fields.CharField(max_length=100, description="盾构机编号", null=True)
    take_time = fields.CharField(max_length=100, description="耗时", null=True)
    time = fields.BigIntField(description="时间戳", null=True)
    driver = fields.CharField(max_length=200, null=True, description="司机")
    foreman = fields.CharField(max_length=200, null=True, description="厂长")
    assembler = fields.CharField(max_length=100, null=True, description="拼装工")
    work_time = fields.JSONField(null=True, description="工作时间")
    fault_time = fields.JSONField(null=True, description="故障时间")

    class Meta:
        table = "bar_chart_report"
        app = "ddg_models"
        connection = "ddg_tenant_conn"

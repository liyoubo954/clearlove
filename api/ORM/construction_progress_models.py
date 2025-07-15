from tortoise.models import Model
from tortoise import fields

class construction_progress(Model):
    id = fields.IntField(pk=True, description="编号")
    shield_id = fields.CharField(max_length=100, description="盾构机编号", null=False)
    pro_name = fields.CharField(max_length=50, description="区间名称", null=False)
    sub_code = fields.CharField(max_length=255, description="施工区间编码", null=True)
    interval_length = fields.DecimalField(max_digits=10, decimal_places=3, description="区间长度", null=True)
    start_time = fields.DateField(description="始发时间", null=True)
    today_ring = fields.DecimalField(max_digits=10, decimal_places=3, description="今日进度-环", null=True)
    today_schedule = fields.DecimalField(max_digits=10, decimal_places=3, description="今日进度-m", null=True)
    plan_ring = fields.DecimalField(max_digits=10, decimal_places=3, description="计划进度-环", null=True)
    plan_schedule = fields.DecimalField(max_digits=10, decimal_places=3, description="计划进度-m", null=True)
    accumulate_ring = fields.DecimalField(max_digits=10, decimal_places=3, description="开累进度-环", null=True)
    accumulate_day = fields.IntField(description="累计天数-天", null=True)
    avg_schedule = fields.DecimalField(max_digits=10, decimal_places=2, description="平均日进度-m", null=True)

    class Meta:
        table = "construction_progress"
        default_connection = "ecust_ddg_conn"

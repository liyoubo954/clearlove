from tortoise import fields, models

class project_stats(models.Model):
    id = fields.IntField(pk=True)
    project_name = fields.CharField(max_length=255, null=True)
    work_area = fields.CharField(max_length=255, null=True)
    bid_money = fields.CharField(max_length=255, null=True)
    bid_time = fields.CharField(max_length=255, null=True)
    finish_time = fields.CharField(max_length=255, null=True)
    tunnel_length = fields.CharField(max_length=50, null=True)
    tube_outer_diameter = fields.CharField(max_length=255, null=True)
    through_waters = fields.CharField(max_length=50, null=True)
    max_excavation_diameter = fields.CharField(max_length=50, null=True)
    project_type = fields.CharField(max_length=50, null=True)
    job_schedule = fields.CharField(max_length=255, null=True)
    type = fields.CharField(max_length=255, null=True)
    company_name = fields.CharField(max_length=255, null=True)
    province = fields.CharField(max_length=255, null=True)
    remark = fields.CharField(max_length=50, null=True)
    pro_code = fields.CharField(max_length=255, null=True)
    sub_code = fields.CharField(max_length=255, null=True)
    through_assise = fields.CharField(max_length=255, null=True)
    hydraulic_pressure = fields.CharField(max_length=255, null=True)
    intension = fields.CharField(max_length=255, null=True)
    duct_piece = fields.CharField(max_length=255, null=True)
    zone_id = fields.BigIntField(null=True)

    class Meta:
        table = "project_stats"
        default_connection = "ecust_ddg_conn"
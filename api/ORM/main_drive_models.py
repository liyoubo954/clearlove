from tortoise import fields, models

class main_drive_stats(models.Model):
    id = fields.IntField(pk=True)
    shield_number = fields.CharField(max_length=55, null=True)
    segment_outside_diameter = fields.CharField(max_length=55, null=True)
    manufacturer = fields.CharField(max_length=255, null=True)
    purchase_time = fields.CharField(max_length=255, null=True)
    participation_project = fields.CharField(max_length=255, null=True)
    time_departure = fields.CharField(max_length=255, null=True)
    receipt_time = fields.CharField(max_length=255, null=True)
    design_length = fields.CharField(max_length=255, null=True)
    length_under_construction = fields.CharField(max_length=255, null=True)
    cumulative_construction_length = fields.CharField(max_length=255, null=True)
    main_drive_running_time = fields.CharField(max_length=255, null=True)
    cumulative_running_time = fields.CharField(max_length=255, null=True)
    remark = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "main_drive_stats"
        default_connection = "ecust_ddg_conn"
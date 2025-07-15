from tortoise import fields, models

class Tunneling_Instruction_Table(models.Model):
    id = fields.IntField(pk=True, description="自增编号")
    project_code = fields.CharField(max_length=10, null=False, description="盾构机编号")
    project_name = fields.CharField(max_length=100, null=False, description="项目名称")
    ring_number = fields.IntField(null=True, description="环号")
    cutting_face_mileage = fields.CharField(max_length=20, null=True, description="切口里程")
    cover_thickness = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="覆土厚度 (m)")
    notch_water_pressure = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="切口水压 (bar)")
    total_thrust = fields.CharField(max_length=10, null=True, description="总推力 (KN)")
    total_torque = fields.CharField(max_length=5, null=True, description="总扭矩 (MN·m)")
    tunneling_speed = fields.CharField(max_length=10, null=True, description="掘进速度 (mm/min)")
    cutterhead_speed = fields.DecimalField(max_digits=3, decimal_places=2, null=True, description="刀盘转速 (rpm)")
    slurry_ratio = fields.CharField(max_length=10, null=True, description="进/排浆比重 (g/cm³)")
    slurry_flow = fields.CharField(max_length=10, null=True, description="进/排浆流量 (m³/h)")
    sync_grouting_pressure_1 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆压力1#(bar)")
    sync_grouting_volume_1 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆量1#(m³)")
    sync_grouting_pressure_2 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆压力2#(bar)")
    sync_grouting_volume_2 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆量2#(m³)")
    sync_grouting_pressure_3 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆压力3#(bar)")
    sync_grouting_volume_3 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆量3#(m³)")
    sync_grouting_pressure_4 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆压力4#(bar)")
    sync_grouting_volume_4 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆量4#(m³)")
    sync_grouting_pressure_5 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆压力5#(bar)")
    sync_grouting_volume_5 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆量5#(m³)")
    sync_grouting_pressure_6 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆压力6#(bar)")
    sync_grouting_volume_6 = fields.DecimalField(max_digits=5, decimal_places=2, null=True, description="同步注浆量6#(m³)")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")
    excel_path = fields.CharField(max_length=50, null=True, description="上传excel到minio, 本列存路径")

    class Meta:
        table = "Tunneling_Instruction_Table"
        default_connection = "ecust_ddg_conn"
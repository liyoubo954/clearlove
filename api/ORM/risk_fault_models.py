from tortoise.models import Model
from tortoise import fields

class risk_fault_records(Model):
    id = fields.IntField(pk=True, description="自增主键")
    connect_key = fields.CharField(max_length=255, null=True, description="盾构机编号")
    ring = fields.IntField(null=True, description="施工环号")
    sub_code = fields.CharField(max_length=255, null=True, description="施工区间编码")
    sub_name = fields.CharField(max_length=255, null=True, description="施工区间名称")
    risk_start_end_ring = fields.CharField(max_length=255, null=True, description="风险源起止环号")
    risk_type = fields.CharField(max_length=255, null=True, description="风险类型")
    risk_content = fields.CharField(max_length=255, null=True, description="风险源信息")
    risk_level = fields.CharField(max_length=255, null=True, description="风险等级")
    risk_desc = fields.CharField(max_length=255, null=True, description="风险描述")
    risk_prevention = fields.CharField(max_length=255, null=True, description="预防措施")
    risk_treatment = fields.CharField(max_length=255, null=True, description="处理方法")
    risk_impact = fields.CharField(max_length=255, null=True, description="对工程的影响")
    risk_early_warning = fields.CharField(max_length=255, null=True, description="风险预警指标")
    risk_early_warning_value = fields.CharField(max_length=255, null=True, description="风险预警值")
    risk_monitoring_frequency = fields.CharField(max_length=255, null=True, description="监测频率")
    surface_settlement_monitoring_value = fields.CharField(max_length=255, null=True, description="地表沉降监测值")
    structure_deformation_value = fields.CharField(max_length=255, null=True, description="建构筑物变形值")
    alarm_ring_section = fields.CharField(max_length=255, null=True, description="警报所在环号")
    alarm_type = fields.CharField(max_length=255, null=True, description="警报类型")
    fault_occurrence_time = fields.CharField(max_length=255, null=True, description="故障发生时间")
    specific_fault_equipment = fields.CharField(max_length=255, null=True, description="故障具体设备")
    fault_type = fields.CharField(max_length=255, null=True, description="故障类型")
    fault_treatment_measures = fields.CharField(max_length=255, null=True, description="故障处理措施")
    sg_fssj = fields.CharField(max_length=255, null=True, description="事故发生时间")
    sg_yy = fields.CharField(max_length=255, null=True, description="事故原因")
    cl_jg = fields.CharField(max_length=255, null=True, description="处理结果")
    wx_yy = fields.CharField(max_length=255, null=True, description="维修原因")
    wx_nr = fields.CharField(max_length=255, null=True, description="维修内容")

    class Meta:
        table = "risk_fault_records"
        default_connection = "ecust_ddg_conn"
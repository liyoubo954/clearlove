from tortoise.models import Model
from tortoise import fields

class segment_info(Model):
    id = fields.IntField(pk=True, description="自增主键")
    connect_key = fields.CharField(max_length=255, null=True, description="盾构机编号")
    ring = fields.IntField(null=True, description="对应施工环号")
    sub_code = fields.CharField(max_length=255, null=True, description="施工区间编码")
    sub_name = fields.CharField(max_length=255, null=True, description="施工区间名称")
    gp_nj = fields.CharField(max_length=255, null=True, description="管片内径")
    gp_wj = fields.CharField(max_length=255, null=True, description="管片外径")
    gp_kd = fields.CharField(max_length=255, null=True, description="管片宽度")
    gp_fks = fields.CharField(max_length=255, null=True, description="管片分块数")
    dw_sppc = fields.CharField(max_length=255, null=True, description="盾尾水平偏差")
    ds_szpc = fields.CharField(max_length=255, null=True, description="盾首竖直偏差")
    gdj = fields.CharField(max_length=255, null=True, description="滚动角")
    dg_dta = fields.CharField(max_length=255, null=True, description="盾构设计曲线DTA")
    gp_pjdw = fields.CharField(max_length=255, null=True, description="管片拼接点位")
    gp_cql = fields.CharField(max_length=255, null=True, description="管片超前量")
    gp_zt = fields.CharField(max_length=255, null=True, description="管片姿态")

    class Meta:
        table = "segment_info"
        default_connection = "ecust_ddg_conn"
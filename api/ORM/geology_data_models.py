from tortoise.models import Model
from tortoise import fields

class geology_data(Model):
    id = fields.IntField(pk=True)
    connect_key = fields.CharField(max_length=255, null=True, description="盾构机编号")
    ring = fields.IntField(null=True, description="对应施工环号")
    sub_code = fields.CharField(max_length=255, null=True, description="对应施工区间编码")
    sub_name = fields.CharField(max_length=255, null=True, description="对应施工区间名称")
    layer_name = fields.CharField(max_length=16, null=True, description="地层名称")
    type = fields.CharField(max_length=16, null=True, description="地层类型")
    soil_surface_params = fields.CharField(max_length=255, null=True, description="土体（开挖面）参数")
    cover_thickness = fields.CharField(max_length=255, null=True, description="覆盖层厚度")
    water_level = fields.CharField(max_length=255, null=True, description="水位线高度")
    permeability = fields.CharField(max_length=255, null=True, description="渗透系数")
    cohesion = fields.CharField(max_length=255, null=True, description="粘聚力")
    internal_friction = fields.CharField(max_length=255, null=True, description="内摩擦角")
    deformation_modulus = fields.CharField(max_length=255, null=True, description="变形模量")
    poissons_ratio = fields.CharField(max_length=255, null=True, description="泊松比")
    lateral_pressure = fields.CharField(max_length=255, null=True, description="侧压力系数")
    overlying_soil_params = fields.CharField(max_length=255, null=True, description="上覆土层参数")
    water_content = fields.FloatField(null=True, description="天然含水量")
    sol_specific_gravity = fields.FloatField(null=True, description="土粒比重")
    natural_porosity_ratio = fields.FloatField(null=True, description="孔隙比")
    liquid_limit = fields.FloatField(null=True, description="液限")
    plastic_limit = fields.FloatField(null=True, description="塑限")
    plasticity_index = fields.FloatField(null=True, description="塑性指数")
    liquidity_index = fields.FloatField(null=True, description="液性指数")
    compression_coefficient = fields.FloatField(null=True, description="压缩系数")
    compression_modulus = fields.FloatField(null=True, description="压缩模量")
    quick_shear_friction_angle = fields.FloatField(null=True, description="快剪摩擦角")
    quick_shear_cohesion = fields.FloatField(null=True, description="快剪粘聚力")
    consolidated_friction_angle = fields.FloatField(null=True, description="固结摩擦角")

    class Meta:
        table = "geology_data"
        default_connection = "ecust_ddg_conn"

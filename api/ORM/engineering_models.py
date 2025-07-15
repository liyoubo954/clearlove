from tortoise.models import Model
from tortoise import fields

class engineering_params(Model):
    id = fields.IntField(pk=True)
    instanceid = fields.IntField(null=True)
    sub_code = fields.CharField(max_length=50, null=True)
    pro_code = fields.CharField(max_length=50, null=True)
    pro_name = fields.CharField(max_length=100, null=True)
    max_diameter = fields.IntField(null=True)
    rube_outerdiameter = fields.IntField(null=True)
    rube_innerdiameter = fields.IntField(null=True)
    rube_thick = fields.IntField(null=True)
    rube_width = fields.IntField(null=True)
    geocondition = fields.CharField(max_length=100, null=True)
    remark = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "engineering_params"
        default_connection = "ecust_ddg_conn"
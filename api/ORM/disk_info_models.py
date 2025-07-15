from tortoise.models import Model
from tortoise import fields
from datetime import datetime

class disk_info(Model):
    ID = fields.IntField(pk=True)
    CONNECT_KEY = fields.CharField(max_length=255, null=True)
    DISK_TYPE = fields.CharField(max_length=255, null=True, description="刀盘形式")
    KNIFE_DISTANCE = fields.CharField(max_length=255, null=True, description="刀间距")
    CUTTER_HEIGHT_DIFFERENCE = fields.CharField(max_length=255, null=True, description="刀高差")
    CHANGE_LOG = fields.CharField(max_length=255, null=True, description="换刀记录")
    KNIFE_STATUS = fields.CharField(max_length=255, null=True, description="刀具状态")
    ABRASION = fields.CharField(max_length=255, null=True, description="磨损量")
    CUTTER_HOB = fields.CharField(max_length=255, null=True, description="滚刀")
    GD_CC = fields.CharField(max_length=255, null=True, description="滚刀尺寸")
    CUT_KNIFE = fields.CharField(max_length=255, null=True, description="切刀")
    CUT_KNIFE_HEIGHT = fields.CharField(max_length=255, null=True, description="切刀刀高")
    LACING_KNIFE = fields.CharField(max_length=255, null=True, description="撕裂刀")
    LACING_KNIFE_HEIGHT = fields.CharField(max_length=255, null=True, description="撕裂刀刀高")
    CREATE_TIME = fields.DatetimeField(null=True, description="创建时间")
    CREATE_BY = fields.CharField(max_length=255, null=True, description="创建者")
    KNIFE_TYPE = fields.CharField(max_length=255, null=True, description="刀具类型")
    KNIFE_LAYOUT = fields.CharField(max_length=255, null=True, description="刀具轨迹布置")
    DP_ZTL = fields.CharField(max_length=255, null=True, description="刀盘总推力")
    DP_NJ = fields.CharField(max_length=255, null=True, description="刀盘扭矩")
    DP_ZS = fields.CharField(max_length=255, null=True, description="刀盘转速")
    DP_GRD = fields.CharField(max_length=255, null=True, description="刀盘贯入度")
    DP_ZJCL = fields.CharField(max_length=255, null=True, description="刀盘总接触力")

    class Meta:
        table = "disk_info"
        default_connection = "ecust_ddg_conn"

    @classmethod
    async def create_with_timestamp(cls, data):
        if 'CREATE_TIME' in data and isinstance(data['CREATE_TIME'], (int, str)):
            try:
                timestamp = int(data['CREATE_TIME'])
                data['CREATE_TIME'] = datetime.fromtimestamp(timestamp)
            except (ValueError, TypeError):
                raise ValueError("无效的时间戳格式")
        return await cls.create(**data)
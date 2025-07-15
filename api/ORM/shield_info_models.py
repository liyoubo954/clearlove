from tortoise.models import Model
from tortoise import fields

class shield_info(Model):
    id = fields.IntField(pk=True)
    connect_key = fields.CharField(max_length=255, description="盾构机编号", null=False)
    sub_code = fields.CharField(max_length=255, description="施工区间编码", null=False)
    sub_name = fields.CharField(max_length=255, description="施工区间名称", null=False)
    ring = fields.IntField(description="施工环号", null=True)
    record_time = fields.CharField(max_length=255, description="记录时间", null=True)
    device_roll = fields.CharField(max_length=255, description="设备侧滚", null=True)
    device_pitch = fields.CharField(max_length=255, description="设备倾角", null=True)
    main_drive_speed = fields.CharField(max_length=255, description="主驱动转速", null=True)
    main_drive_torque = fields.CharField(max_length=255, description="主驱动扭矩", null=True)
    main_drive_temp = fields.CharField(max_length=255, description="主驱动温度", null=True)
    main_drive_current = fields.CharField(max_length=255, description="主驱动电流", null=True)
    main_drive_grease = fields.CharField(max_length=255, description="主驱动密封油脂量", null=True)
    kwc_prs = fields.CharField(max_length=255, description="开挖仓压力", null=True)
    gzc_prs = fields.CharField(max_length=255, description="工作仓压力", null=True)
    tjyg_prs = fields.CharField(max_length=255, description="推进油缸压力", null=True)
    ztl = fields.CharField(max_length=255, description="总推力", null=True)
    fqyg_prs = fields.CharField(max_length=255, description="分区油缸压力", null=True)
    yg_tl = fields.CharField(max_length=255, description="油缸推力", null=True)
    yggz_prs = fields.CharField(max_length=255, description="油缸工作压力", null=True)
    yg_xc = fields.CharField(max_length=255, description="油缸行程", null=True)
    jj_prs = fields.CharField(max_length=255, description="进浆压力", null=True)
    cj_prs = fields.CharField(max_length=255, description="出浆压力", null=True)
    nj_md = fields.CharField(max_length=255, description="泥浆密度", null=True)
    nj_nd = fields.CharField(max_length=255, description="泥浆粘度", null=True)
    nj_jflow = fields.CharField(max_length=255, description="进浆流量", null=True)
    lxj_nj = fields.CharField(max_length=255, description="螺旋机扭矩", null=True)
    lxj_prs = fields.CharField(max_length=255, description="螺旋机压力", null=True)
    zj_prs = fields.CharField(max_length=255, description="注浆压力", null=True)
    zjl = fields.CharField(max_length=255, description="注浆量", null=True)
    jy_lx = fields.CharField(max_length=255, description="浆液类型", null=True)
    yzzr_prs = fields.CharField(max_length=255, description="油脂注入压力", null=True)
    main_drive_tail_seal_grease = fields.CharField(max_length=255, description="主驱动盾尾密封油脂消耗量", null=True)

    class Meta:
        table = "shield_info"
        default_connection = "ecust_ddg_conn"
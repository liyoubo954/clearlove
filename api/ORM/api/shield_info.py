from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from shield_info_models import shield_info
from tortoise.expressions import Q
from pydantic import BaseModel

shield_info_api = APIRouter()

class ShieldInfoIn(BaseModel):
    connect_key: str
    sub_code: str
    sub_name: str
    ring: Optional[int] = None
    record_time: Optional[str] = None
    device_roll: Optional[str] = None
    device_pitch: Optional[str] = None
    main_drive_speed: Optional[str] = None
    main_drive_torque: Optional[str] = None
    main_drive_temp: Optional[str] = None
    main_drive_current: Optional[str] = None
    main_drive_grease: Optional[str] = None
    kwc_prs: Optional[str] = None
    gzc_prs: Optional[str] = None
    tjyg_prs: Optional[str] = None
    ztl: Optional[str] = None
    fqyg_prs: Optional[str] = None
    yg_tl: Optional[str] = None
    yggz_prs: Optional[str] = None
    yg_xc: Optional[str] = None
    jj_prs: Optional[str] = None
    cj_prs: Optional[str] = None
    nj_md: Optional[str] = None
    nj_nd: Optional[str] = None
    nj_jflow: Optional[str] = None
    lxj_nj: Optional[str] = None
    lxj_prs: Optional[str] = None
    zj_prs: Optional[str] = None
    zjl: Optional[str] = None
    jy_lx: Optional[str] = None
    yzzr_prs: Optional[str] = None
    main_drive_tail_seal_grease: Optional[str] = None

@shield_info_api.post("/shield_info")
async def add_shield_info(info_in: ShieldInfoIn):
    try:
        new_info = await shield_info.create(**info_in.dict(exclude_unset=True))
        return {"status": 0, "msg": "添加成功", "data": {"id": new_info.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建掘进参数失败: {str(e)}")

@shield_info_api.get("/shield_info_list")
async def get_shield_info_list(
    id: Optional[int] = Query(None, description="编号"),
    connect_key: Optional[str] = Query(None, description="盾构机编号"),
    sub_code: Optional[str] = Query(None, description="工点编码"),
    sub_name: Optional[str] = Query(None, description="工点名称"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    filters = Q()
    if id is not None:
        filters &= Q(id=id)
    if connect_key:
        filters &= Q(connect_key=connect_key)
    if sub_code:
        filters &= Q(sub_code=sub_code)
    if sub_name:
        filters &= Q(sub_name=sub_name)

    total = await shield_info.filter(filters).count()
    records = await shield_info.filter(filters).offset((page - 1) * per_page).limit(per_page).all()
    
    return {
        "status": 0,
        "msg": "获取成功",
        "data": {
            "items": records,
            "total": total
        }
    }

class ShieldInfoUpdateModel(BaseModel):
    id: int
    connect_key: str
    sub_code: str
    sub_name: str
    ring: Optional[int] = None
    record_time: Optional[str] = None
    device_roll: Optional[str] = None
    device_pitch: Optional[str] = None
    main_drive_speed: Optional[str] = None
    main_drive_torque: Optional[str] = None
    main_drive_temp: Optional[str] = None
    main_drive_current: Optional[str] = None
    main_drive_grease: Optional[str] = None
    kwc_prs: Optional[str] = None
    gzc_prs: Optional[str] = None
    tjyg_prs: Optional[str] = None
    ztl: Optional[str] = None
    fqyg_prs: Optional[str] = None
    yg_tl: Optional[str] = None
    yggz_prs: Optional[str] = None
    yg_xc: Optional[str] = None
    jj_prs: Optional[str] = None
    cj_prs: Optional[str] = None
    nj_md: Optional[str] = None
    nj_nd: Optional[str] = None
    nj_jflow: Optional[str] = None
    lxj_nj: Optional[str] = None
    lxj_prs: Optional[str] = None
    zj_prs: Optional[str] = None
    zjl: Optional[str] = None
    jy_lx: Optional[str] = None
    yzzr_prs: Optional[str] = None
    main_drive_tail_seal_grease: Optional[str] = None

@shield_info_api.post("/update_shield_info")
async def update_shield_info(info_data: ShieldInfoUpdateModel):
    try:
        info = await shield_info.get_or_none(id=info_data.id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{info_data.id}的记录"}
        
        await info.update_from_dict(info_data.dict(exclude_unset=True))
        await info.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@shield_info_api.delete("/delete_shield_info/{id}")
async def delete_shield_info(id: int):
    try:
        info = await shield_info.get_or_none(id=id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await info.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from shield_machine_models import shield_machine
from tortoise.expressions import Q
from pydantic import BaseModel

shield_machine_api = APIRouter()

class shieldinfoIn(BaseModel):
    connect_key: str
    ring: int
    sub_code: str
    sub_name: str
    digging_diameter: Optional[str] = None
    total_length: Optional[str] = None
    total_weight: Optional[str] = None
    design_pressure: Optional[str] = None
    working_pressure: Optional[str] = None
    max_thrust: Optional[str] = None
    max_cutter_speed: Optional[str] = None
    DP_XZNJ: Optional[str] = None
    DP_SDNJ: Optional[str] = None
    DP_KKL: Optional[str] = None
    max_advance_speed: Optional[str] = None
    cylinder_layout: Optional[str] = None
    shield_type: Optional[str] = None
    construction_loc: Optional[str] = None
    start_end_section: Optional[str] = None
    ring_segment_size: Optional[str] = None
    tail_brush_count: Optional[str] = None
    tail_gap: Optional[str] = None
    grease_pressure: Optional[str] = None
    yzcs: Optional[str] = None
    gd_cc: Optional[str] = None
    gd_sl: Optional[str] = None
    jy_ls: Optional[str] = None
    jy_nd: Optional[str] = None
    cz_ll: Optional[str] = None
    jb_psxs: Optional[str] = None
    flushing_nozzle_quantity: Optional[str] = None
    flushing_nozzle_type: Optional[str] = None
    flushing_flow: Optional[str] = None
    property_unit: Optional[str] = None
    project_status: Optional[str] = None
    equipment_property: Optional[str] = None
    equipment_brand: Optional[str] = None
    segment_outside_diameter: Optional[str] = None
    segment_width: Optional[str] = None
    manufacturer: Optional[str] = None

@shield_machine_api.post("/shield_machine")
async def add_shield_info(info_in: shieldinfoIn):
    try:
        new_info = await shield_machine.create(**info_in.dict(exclude_unset=True))
        return {"status": 0, "msg": "添加成功", "data": {"id": new_info.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建盾构机基本信息失败: {str(e)}")

@shield_machine_api.get("/shield_machine_list")
async def get_shield_machine_list(
    connect_key: Optional[str] = Query(None, description="盾构机编号"),
    ring: Optional[int] = Query(None, description="施工环号"),
    sub_code: Optional[str] = Query(None, description="施工区间编码"),
    sub_name: Optional[str] = Query(None, description="施工区间名称"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    filters = Q()
    if connect_key:
        filters &= Q(connect_key=connect_key)
    if ring is not None:
        filters &= Q(ring=ring)
    if sub_code:
        filters &= Q(sub_code=sub_code)
    if sub_name:
        filters &= Q(sub_name=sub_name)

    total = await shield_machine.filter(filters).count()
    items = await shield_machine.filter(filters).offset((page - 1) * per_page).limit(per_page)

    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": [item for item in items],
            "total": total,
            "page": page,
            "per_page": per_page
        }
    }

class shieldinfoUpdateModel(BaseModel):
    id: int
    connect_key: str
    ring: int
    sub_code: str
    sub_name: str
    digging_diameter: Optional[str] = None
    total_length: Optional[str] = None
    total_weight: Optional[str] = None
    design_pressure: Optional[str] = None
    working_pressure: Optional[str] = None
    max_thrust: Optional[str] = None
    max_cutter_speed: Optional[str] = None
    DP_XZNJ: Optional[str] = None
    DP_SDNJ: Optional[str] = None
    DP_KKL: Optional[str] = None
    max_advance_speed: Optional[str] = None
    cylinder_layout: Optional[str] = None
    shield_type: Optional[str] = None
    construction_loc: Optional[str] = None
    start_end_section: Optional[str] = None
    ring_segment_size: Optional[str] = None
    tail_brush_count: Optional[str] = None
    tail_gap: Optional[str] = None
    grease_pressure: Optional[str] = None
    yzcs: Optional[str] = None
    gd_cc: Optional[str] = None
    gd_sl: Optional[str] = None
    jy_ls: Optional[str] = None
    jy_nd: Optional[str] = None
    cz_ll: Optional[str] = None
    jb_psxs: Optional[str] = None
    flushing_nozzle_quantity: Optional[str] = None
    flushing_nozzle_type: Optional[str] = None
    flushing_flow: Optional[str] = None
    property_unit: Optional[str] = None
    project_status: Optional[str] = None
    equipment_property: Optional[str] = None
    equipment_brand: Optional[str] = None
    segment_outside_diameter: Optional[str] = None
    segment_width: Optional[str] = None
    manufacturer: Optional[str] = None

@shield_machine_api.post("/update_shield_machine")
async def update_shield_info(info_data: shieldinfoUpdateModel):
    try:
        info = await shield_machine.get_or_none(id=info_data.id)
        if not info:
            return {"status": 1, "msg": f"未找到id为{info_data.id}的记录"}
        
        await info.update_from_dict(info_data.dict(exclude_unset=True))
        await info.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@shield_machine_api.delete("/delete_shield_machine/{id}")
async def delete_shield_info(id: int):
    try:
        info = await shield_machine.get_or_none(id=id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await info.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
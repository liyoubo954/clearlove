from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from main_drive_models import main_drive_stats
from tortoise.expressions import Q
from pydantic import BaseModel

main_drive_api = APIRouter()

class maindriveIn(BaseModel):
    shield_number: str
    segment_outside_diameter: str
    manufacturer: str
    purchase_time: str
    participation_project: Optional[str] = None
    time_departure: Optional[str] = None
    receipt_time: Optional[str] = None
    design_length: Optional[str] = None
    length_under_construction: Optional[str] = None
    cumulative_construction_length: Optional[str] = None
    main_drive_running_time: Optional[str] = None
    cumulative_running_time: Optional[str] = None
    remark: Optional[str] = None

class maindriveUpdateIn(BaseModel):
    id: int
    shield_number: str
    segment_outside_diameter: str
    manufacturer: str
    purchase_time: str
    participation_project: Optional[str] = None
    time_departure: Optional[str] = None
    receipt_time: Optional[str] = None
    design_length: Optional[str] = None
    length_under_construction: Optional[str] = None
    cumulative_construction_length: Optional[str] = None
    main_drive_running_time: Optional[str] = None
    cumulative_running_time: Optional[str] = None
    remark: Optional[str] = None

@main_drive_api.post("/main_drive")
async def add_main_drive(info_in: maindriveIn):
    try:
        new_info = await main_drive_stats.create(**info_in.dict(exclude_unset=True))
        return {"status": 0, "msg": "添加成功", "data": {"id": new_info.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"添加失败: {str(e)}")

@main_drive_api.get("/main_drive_list")
async def get_main_drive_list(
    id: Optional[int] = Query(None, description="编号"),
    shield_number: Optional[str] = Query(None, description="盾构机编号"),
    manufacturer: Optional[str] = Query(None, description="制造商"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    filters = Q()
    if id is not None:
        filters &= Q(id=id)
    if shield_number:
        filters &= Q(shield_number=shield_number)
    if manufacturer:
        filters &= Q(manufacturer=manufacturer)

    total = await main_drive_stats.filter(filters).count()
    records = await main_drive_stats.filter(filters).offset((page - 1) * per_page).limit(per_page).all()
    
    return {
        "status": 0,
        "msg": "获取成功",
        "data": {
            "items": records,
            "total": total
        }
    }

@main_drive_api.post("/update_main_drive")
async def update_main_drive(info_in: maindriveUpdateIn):
    try:
        info = await main_drive_stats.get_or_none(id=info_in.id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{info_in.id}的记录"}
        
        await info.update_from_dict(info_in.dict(exclude_unset=True))
        await info.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@main_drive_api.delete("/delete_main_drive/{id}")
async def delete_main_drive(id: int):
    try:
        info = await main_drive_stats.get_or_none(id=id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await info.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
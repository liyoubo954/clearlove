from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from construction_progress_models import construction_progress
from tortoise.expressions import Q
from pydantic import BaseModel
from datetime import datetime

construction_progress_api = APIRouter()

class constructionprogressIn(BaseModel):
    shield_id: str
    pro_name: str
    start_time: str
    sub_code: Optional[str] = None
    interval_length: Optional[float] = None
    today_ring: Optional[float] = None
    today_schedule: Optional[float] = None
    plan_ring: Optional[float] = None
    plan_schedule: Optional[float] = None
    accumulate_ring: Optional[float] = None
    accumulate_day: Optional[int] = None
    avg_schedule: Optional[float] = None

class ConstructionProgressUpdateModel(BaseModel):
    id: int
    shield_id: str
    pro_name: str
    start_time: str
    sub_code: Optional[str] = None
    interval_length: Optional[float] = None
    today_ring: Optional[float] = None
    today_schedule: Optional[float] = None
    plan_ring: Optional[float] = None
    plan_schedule: Optional[float] = None
    accumulate_ring: Optional[float] = None
    accumulate_day: Optional[int] = None
    avg_schedule: Optional[float] = None

@construction_progress_api.post("/progress")
async def create_construction_progress(progress_data: constructionprogressIn):
    try:
        data = progress_data.dict(exclude_unset=True)
        if "start_time" in data:
            try:
                data["start_time"] = datetime.strptime(data["start_time"], "%Y-%m-%d").date()
            except ValueError as e:
                raise HTTPException(status_code=400, detail=f"日期格式错误，请使用YYYY-MM-DD格式: {str(e)}")
        await construction_progress.create(**data)
        return {"status": 0, "msg": "添加成功"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"添加失败: {str(e)}")

@construction_progress_api.get("/progress_list")
async def get_construction_progress_list(
    shield_id: Optional[str] = Query(None, description="盾构机编号"),
    pro_name: Optional[str] = Query(None, description="区间名称"),
    sub_code: Optional[str] = Query(None, description="施工区间编码"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    filters = Q()
    if shield_id:
        filters &= Q(shield_id=shield_id)
    if pro_name:
        filters &= Q(pro_name=pro_name)
    if sub_code:
        filters &= Q(sub_code=sub_code)

    total = await construction_progress.filter(filters).count()
    items = await construction_progress.filter(filters) \
        .offset((page - 1) * per_page) \
        .limit(per_page) \
        .values()

    return {
        "status": 0,
        "msg": "获取成功",
        "data": {
            "items": items,
            "total": total,
            "page": page,
            "per_page": per_page
        }
    }

@construction_progress_api.post("/update_progress")
async def update_construction_progress(progress_data: ConstructionProgressUpdateModel):
    try:
        progress = await construction_progress.get_or_none(id=progress_data.id)
        if not progress:
            return {"status": 1, "msg": f"未找到ID为{progress_data.id}的记录"}
        
        data = progress_data.dict(exclude_unset=True)
        if "start_time" in data:
            try:
                data["start_time"] = datetime.strptime(data["start_time"], "%Y-%m-%d").date()
            except ValueError as e:
                raise HTTPException(status_code=400, detail=f"日期格式错误，请使用YYYY-MM-DD格式: {str(e)}")
        
        await progress.update_from_dict(data)
        await progress.save()
        return {"status": 0, "msg": "更新成功"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@construction_progress_api.delete("/delete_progress/{id}")
async def delete_construction_progress(id: int):
    try:
        progress = await construction_progress.get_or_none(id=id)
        if not progress:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await progress.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from project_stats_models import project_stats
from tortoise.expressions import Q
from pydantic import BaseModel

project_stats_api = APIRouter()

class projectstatsIn(BaseModel):
    id: Optional[int] = None
    project_name: str  # 保持必填
    work_area: str  # 保持必填
    bid_money: Optional[str] = None
    bid_time: Optional[str] = None
    finish_time: Optional[str] = None
    tunnel_length: Optional[str] = None
    tube_outer_diameter: Optional[str] = None
    through_waters: Optional[str] = None
    max_excavation_diameter: Optional[str] = None
    project_type: Optional[str] = None
    job_schedule: Optional[str] = None
    type: Optional[str] = None
    company_name: Optional[str] = None
    province: Optional[str] = None
    remark: Optional[str] = None
    pro_code: Optional[str] = None
    sub_code: Optional[str] = None
    through_assise: Optional[str] = None
    hydraulic_pressure: Optional[str] = None
    intension: Optional[str] = None
    duct_piece: Optional[str] = None
    zone_id: Optional[int] = None

class projectstatsupdatemodel(BaseModel):
    id: int  # ID是必填的，用于更新记录
    project_name: Optional[str] = None
    work_area: Optional[str] = None
    bid_money: Optional[str] = None
    bid_time: Optional[str] = None
    finish_time: Optional[str] = None
    tunnel_length: Optional[str] = None
    tube_outer_diameter: Optional[str] = None
    through_waters: Optional[str] = None
    max_excavation_diameter: Optional[str] = None
    project_type: Optional[str] = None
    job_schedule: Optional[str] = None
    type: Optional[str] = None
    company_name: Optional[str] = None
    province: Optional[str] = None
    remark: Optional[str] = None
    pro_code: Optional[str] = None
    sub_code: Optional[str] = None
    through_assise: Optional[str] = None
    hydraulic_pressure: Optional[str] = None
    intension: Optional[str] = None
    duct_piece: Optional[str] = None
    zone_id: Optional[int] = None

@project_stats_api.post("/project_stats")
async def add_project_stats(stats_in: projectstatsIn):
    try:
        new_stats = await project_stats.create(**stats_in.dict(exclude_unset=True))
        return {"status": 0, "msg": "添加成功", "data": {"id": new_stats.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建项目统计失败: {str(e)}")

@project_stats_api.get("/project_stats_list")
async def get_project_stats_list(
    id: Optional[int] = Query(None, description="编号"),
    project_name: Optional[str] = Query(None, description="项目名称"),
    work_area: Optional[str] = Query(None, description="工区"),
    pro_code: Optional[str] = Query(None, description="项目编码"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    filters = Q()
    if id is not None:
        filters &= Q(id=id)
    if project_name:
        filters &= Q(project_name=project_name)
    if work_area:
        filters &= Q(work_area=work_area)
    if pro_code:
        filters &= Q(pro_code=pro_code)

    total = await project_stats.filter(filters).count()
    items = await project_stats.filter(filters)\
        .offset((page - 1) * per_page)\
        .limit(per_page)

    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": [{
                "id": item.id,
                "project_name": item.project_name,
                "work_area": item.work_area,
                "bid_money": item.bid_money,
                "bid_time": item.bid_time,
                "finish_time": item.finish_time,
                "tunnel_length": item.tunnel_length,
                "tube_outer_diameter": item.tube_outer_diameter,
                "through_waters": item.through_waters,
                "max_excavation_diameter": item.max_excavation_diameter,
                "project_type": item.project_type,
                "job_schedule": item.job_schedule,
                "type": item.type,
                "company_name": item.company_name,
                "province": item.province,
                "remark": item.remark,
                "pro_code": item.pro_code,
                "sub_code": item.sub_code,
                "through_assise": item.through_assise,
                "hydraulic_pressure": item.hydraulic_pressure,
                "intension": item.intension,
                "duct_piece": item.duct_piece,
                "zone_id": item.zone_id
            } for item in items],
            "total": total,
            "page": page,
            "per_page": per_page
        }
    }

@project_stats_api.post("/update_project_stats")
async def update_project_stats(stats_data: projectstatsupdatemodel):
    try:
        stats = await project_stats.get_or_none(id=stats_data.id)
        if not stats:
            return {"status": 1, "msg": f"未找到ID为{stats_data.id}的记录"}
        
        await stats.update_from_dict(stats_data.dict(exclude_unset=True))
        await stats.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@project_stats_api.delete("/delete_project_stats/{id}")
async def delete_project_stats(id: int):
    try:
        stats = await project_stats.get_or_none(id=id)
        if not stats:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await stats.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
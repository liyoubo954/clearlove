from fastapi import APIRouter, Query, HTTPException, Depends
from typing import Optional
from geology_data_models import geology_data
from tortoise.expressions import Q
from pydantic import BaseModel
from Rbac_utils import get_user_from_token, check_permission

geology_data_api = APIRouter()

class GeologyDataIn(BaseModel):
    connect_key: str
    ring: int
    sub_code: str
    sub_name: str
    layer_name: Optional[str] = None
    type: Optional[str] = None
    soil_surface_params: Optional[str] = None
    cover_thickness: Optional[str] = None
    water_level: Optional[str] = None
    permeability: Optional[str] = None
    cohesion: Optional[str] = None
    internal_friction: Optional[str] = None
    deformation_modulus: Optional[str] = None
    poissons_ratio: Optional[str] = None
    lateral_pressure: Optional[str] = None
    overlying_soil_params: Optional[str] = None
    water_content: Optional[float] = None
    sol_specific_gravity: Optional[float] = None
    natural_porosity_ratio: Optional[float] = None
    liquid_limit: Optional[float] = None
    plastic_limit: Optional[float] = None
    plasticity_index: Optional[float] = None
    liquidity_index: Optional[float] = None
    compression_coefficient: Optional[float] = None
    compression_modulus: Optional[float] = None
    quick_shear_friction_angle: Optional[float] = None
    quick_shear_cohesion: Optional[float] = None
    consolidated_friction_angle: Optional[float] = None

@geology_data_api.post("/geology_data")
async def add_geology_data(data_in: GeologyDataIn):
    try:
        new_data = await geology_data.create(**data_in.dict(exclude_unset=True))
        return {"status": 0, "msg": "添加成功", "data": {"id": new_data.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建地质数据失败: {str(e)}")

@geology_data_api.get("/geology_data_list")
async def get_geology_data_list(
    connect_key: Optional[str] = Query(None, description="盾构机编号"),
    sub_code: Optional[str] = Query(None, description="施工区间编码"),
    sub_name: Optional[str] = Query(None, description="施工区间名称"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    filters = Q()
    if connect_key:
        filters &= Q(connect_key=connect_key)
    if sub_code:
        filters &= Q(sub_code=sub_code)
    if sub_name:
        filters &= Q(sub_name=sub_name)

    total = await geology_data.filter(filters).count()
    items = await geology_data.filter(filters)\
        .offset((page - 1) * per_page)\
        .limit(per_page)\
        .all()

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

class GeologyDataUpdateModel(BaseModel):
    id: int
    connect_key: str
    ring: int
    sub_code: str
    sub_name: str
    layer_name: Optional[str] = None
    type: Optional[str] = None
    soil_surface_params: Optional[str] = None
    cover_thickness: Optional[str] = None
    water_level: Optional[str] = None
    permeability: Optional[str] = None
    cohesion: Optional[str] = None
    internal_friction: Optional[str] = None
    deformation_modulus: Optional[str] = None
    poissons_ratio: Optional[str] = None
    lateral_pressure: Optional[str] = None
    overlying_soil_params: Optional[str] = None
    water_content: Optional[float] = None
    sol_specific_gravity: Optional[float] = None
    natural_porosity_ratio: Optional[float] = None
    liquid_limit: Optional[float] = None
    plastic_limit: Optional[float] = None
    plasticity_index: Optional[float] = None
    liquidity_index: Optional[float] = None
    compression_coefficient: Optional[float] = None
    compression_modulus: Optional[float] = None
    quick_shear_friction_angle: Optional[float] = None
    quick_shear_cohesion: Optional[float] = None
    consolidated_friction_angle: Optional[float] = None

@geology_data_api.post("/update_geology_data")
async def update_geology_data(data: GeologyDataUpdateModel):
    try:
        geology = await geology_data.get_or_none(id=data.id)
        if not geology:
            return {"status": 1, "msg": f"未找到ID为{data.id}的记录"}
        
        await geology.update_from_dict(data.dict(exclude_unset=True))
        await geology.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@geology_data_api.delete("/delete_geology_data/{id}")
async def delete_geology_data(id: int):
    try:
        geology = await geology_data.get_or_none(id=id)
        if not geology:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await geology.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
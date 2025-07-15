from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from segment_models import segment_info
from tortoise.expressions import Q
from pydantic import BaseModel

segment_info_api = APIRouter()

class segmentinfoIn(BaseModel):
    connect_key: str
    ring: int
    sub_code: str
    sub_name: str
    gp_nj: Optional[str] = None
    gp_wj: Optional[str] = None
    gp_kd: Optional[str] = None
    gp_fks: Optional[str] = None
    dw_sppc: Optional[str] = None
    ds_szpc: Optional[str] = None
    gdj: Optional[str] = None
    dg_dta: Optional[str] = None
    gp_pjdw: Optional[str] = None
    gp_cql: Optional[str] = None
    gp_zt: Optional[str] = None

@segment_info_api.post("/segment_info")
async def add_segment_info(info_in: segmentinfoIn):
    try:
        new_info = await segment_info.create(**info_in.dict(exclude_unset=True))
        return {"status": 0, "msg": "添加成功", "data": {"id": new_info.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"添加失败: {str(e)}")

@segment_info_api.get("/segment_info_list")
async def get_segment_info_list(
    id: Optional[int] = Query(None, description="编号"),
    connect_key: Optional[str] = Query(None, description="盾构机编码"),
    sub_code: Optional[str] = Query(None, description="施工区间编码"),
    sub_name: Optional[str] = Query(None, description="施工区间名称"),
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

    total = await segment_info.filter(filters).count()
    items = await segment_info.filter(filters).offset((page - 1) * per_page).limit(per_page).all()
    
    # 将数据库对象转换为字典列表
    items_dict = [{
        'id': item.id,
        'connect_key': item.connect_key,
        'ring': item.ring,
        'sub_code': item.sub_code,
        'sub_name': item.sub_name,
        'gp_nj': item.gp_nj,
        'gp_wj': item.gp_wj,
        'gp_kd': item.gp_kd,
        'gp_fks': item.gp_fks,
        'dw_sppc': item.dw_sppc,
        'ds_szpc': item.ds_szpc,
        'gdj': item.gdj,
        'dg_dta': item.dg_dta,
        'gp_pjdw': item.gp_pjdw,
        'gp_cql': item.gp_cql,
        'gp_zt': item.gp_zt
    } for item in items]

    return {
        "status": 0,
        "msg": "获取成功",
        "data": {
            "items": items_dict,
            "total": total,
            "page": page,
            "perPage": per_page,
            "count": total
        }
    }

class SegmentInfoUpdateModel(BaseModel):
    id: int
    connect_key: str
    ring: int
    sub_code: str
    sub_name: str
    gp_nj: Optional[str] = None
    gp_wj: Optional[str] = None
    gp_kd: Optional[str] = None
    gp_fks: Optional[str] = None
    dw_sppc: Optional[str] = None
    ds_szpc: Optional[str] = None
    gdj: Optional[str] = None
    dg_dta: Optional[str] = None
    gp_pjdw: Optional[str] = None
    gp_cql: Optional[str] = None
    gp_zt: Optional[str] = None

@segment_info_api.post("/update_segment_info")
async def update_segment_info(info_data: SegmentInfoUpdateModel):
    try:
        info = await segment_info.get_or_none(id=info_data.id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{info_data.id}的记录"}
        
        await info.update_from_dict(info_data.dict(exclude_unset=True))
        await info.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@segment_info_api.delete("/delete_segment_info/{id}")
async def delete_segment_info(id: int):
    try:
        info = await segment_info.get_or_none(id=id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await info.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
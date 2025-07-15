from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from disk_info_models import disk_info
from tortoise.expressions import Q
from pydantic import BaseModel
from datetime import datetime

disk_info_api = APIRouter()

class diskinfoIn(BaseModel):
    CONNECT_KEY: str
    DISK_TYPE: Optional[str] = None
    KNIFE_DISTANCE: Optional[str] = None
    CUTTER_HEIGHT_DIFFERENCE: Optional[str] = None
    CHANGE_LOG: Optional[str] = None
    KNIFE_STATUS: Optional[str] = None
    ABRASION: Optional[str] = None
    CUTTER_HOB: Optional[str] = None
    GD_CC: Optional[str] = None
    CUT_KNIFE: Optional[str] = None
    CUT_KNIFE_HEIGHT: Optional[str] = None
    LACING_KNIFE: Optional[str] = None
    LACING_KNIFE_HEIGHT: Optional[str] = None
    CREATE_TIME: Optional[datetime] = None
    CREATE_BY: Optional[str] = None
    KNIFE_TYPE: Optional[str] = None
    KNIFE_LAYOUT: Optional[str] = None
    DP_ZTL: Optional[str] = None
    DP_NJ: Optional[str] = None
    DP_ZS: Optional[str] = None
    DP_GRD: Optional[str] = None
    DP_ZJCL: Optional[str] = None

@disk_info_api.post("/disk_info")
async def add_disk_info(info_in: diskinfoIn):
    try:
        data = info_in.dict(exclude_unset=True)
        if 'CREATE_TIME' in data and isinstance(data['CREATE_TIME'], str):
            data['CREATE_TIME'] = datetime.fromisoformat(data['CREATE_TIME'].replace('Z', '+00:00'))
        new_info = await disk_info.create(**data)
        return {"status": 0, "msg": "添加成功", "data": {"ID": new_info.ID}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建刀盘信息失败: {str(e)}")

@disk_info_api.get("/disk_info_list")
async def get_disk_info_list(
    ID: Optional[int] = Query(None, description="编号"),
    CONNECT_KEY: Optional[str] = Query(None, description="盾构机编号"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    filters = Q()
    if ID is not None:
        filters &= Q(ID=ID)
    if CONNECT_KEY:
        filters &= Q(CONNECT_KEY=CONNECT_KEY)

    total = await disk_info.filter(filters).count()
    items = await disk_info.filter(filters).offset((page - 1) * per_page).limit(per_page)

    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": [{
                "ID": item.ID,
                "CONNECT_KEY": item.CONNECT_KEY,
                "DISK_TYPE": item.DISK_TYPE,
                "KNIFE_DISTANCE": item.KNIFE_DISTANCE,
                "CUTTER_HEIGHT_DIFFERENCE": item.CUTTER_HEIGHT_DIFFERENCE,
                "CHANGE_LOG": item.CHANGE_LOG,
                "KNIFE_STATUS": item.KNIFE_STATUS,
                "ABRASION": item.ABRASION,
                "CUTTER_HOB": item.CUTTER_HOB,
                "GD_CC": item.GD_CC,
                "CUT_KNIFE": item.CUT_KNIFE,
                "CUT_KNIFE_HEIGHT": item.CUT_KNIFE_HEIGHT,
                "LACING_KNIFE": item.LACING_KNIFE,
                "LACING_KNIFE_HEIGHT": item.LACING_KNIFE_HEIGHT,
                "CREATE_TIME": item.CREATE_TIME,
                "CREATE_BY": item.CREATE_BY,
                "KNIFE_TYPE": item.KNIFE_TYPE,
                "KNIFE_LAYOUT": item.KNIFE_LAYOUT,
                "DP_ZTL": item.DP_ZTL,
                "DP_NJ": item.DP_NJ,
                "DP_ZS": item.DP_ZS,
                "DP_GRD": item.DP_GRD,
                "DP_ZJCL": item.DP_ZJCL
            } for item in items],
            "total": total,
            "page": page,
            "per_page": per_page
        }
    }

class diskinfoUpdateModel(BaseModel):
    ID: int
    CONNECT_KEY: str
    DISK_TYPE: Optional[str] = None
    KNIFE_DISTANCE: Optional[str] = None
    CUTTER_HEIGHT_DIFFERENCE: Optional[str] = None
    CHANGE_LOG: Optional[str] = None
    KNIFE_STATUS: Optional[str] = None
    ABRASION: Optional[str] = None
    CUTTER_HOB: Optional[str] = None
    GD_CC: Optional[str] = None
    CUT_KNIFE: Optional[str] = None
    CUT_KNIFE_HEIGHT: Optional[str] = None
    LACING_KNIFE: Optional[str] = None
    LACING_KNIFE_HEIGHT: Optional[str] = None
    CREATE_TIME: Optional[datetime] = None
    CREATE_BY: Optional[str] = None
    KNIFE_TYPE: Optional[str] = None
    KNIFE_LAYOUT: Optional[str] = None
    DP_ZTL: Optional[str] = None
    DP_NJ: Optional[str] = None
    DP_ZS: Optional[str] = None
    DP_GRD: Optional[str] = None
    DP_ZJCL: Optional[str] = None

@disk_info_api.post("/update_disk_info")
async def update_disk_info(info_data: diskinfoUpdateModel):
    try:
        info = await disk_info.get_or_none(ID=info_data.ID)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{info_data.ID}的记录"}
        
        data = info_data.dict(exclude_unset=True)
        if 'CREATE_TIME' in data and isinstance(data['CREATE_TIME'], str):
            data['CREATE_TIME'] = datetime.fromisoformat(data['CREATE_TIME'].replace('Z', '+00:00'))
        
        await info.update_from_dict(data)
        await info.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@disk_info_api.delete("/delete_disk_info/{ID}")
async def delete_disk_info(ID: int):
    try:
        info = await disk_info.get_or_none(ID=ID)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{ID}的记录"}
        
        await info.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
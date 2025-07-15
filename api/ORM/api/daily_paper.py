from fastapi import APIRouter, Query, HTTPException, Depends
from typing import Optional
from daily_models import daily_paper
from tortoise.expressions import Q
from pydantic import BaseModel
from Rbac_utils import get_user_from_token, check_permission

daily_paper_api = APIRouter()

class DailyPaperUpdateModel(BaseModel):
    id: int
    areaId: Optional[int] = None
    ljsh: Optional[float] = None
    dpnj: Optional[str] = None
    jjbz: Optional[str] = None
    cjll: Optional[str] = None
    dpzs: Optional[str] = None
    kslc: Optional[float] = None
    qjcd: Optional[float] = None
    tjsd: Optional[str] = None
    jjll: Optional[str] = None
    cjbz: Optional[str] = None
    jrjd: Optional[str] = None
    ztl: Optional[str] = None
    qjyl: Optional[float] = None
    grd: Optional[str] = None
    wcd: Optional[str] = None
    qkyl: Optional[str] = None
    qpcyl: Optional[str] = None
    qjmc: Optional[str] = None
    dgjbh: Optional[str] = None
    pjrjc: Optional[float] = None
    jslc: Optional[float] = None
    sfsj: Optional[str] = None
    time: Optional[str] = None

@daily_paper_api.get("/daily_paper_list")
async def get_daily_paper_list(
    id: Optional[int] = Query(None, description="编号"),
    areaId: Optional[int] = Query(None, description="盾构机编码id"),
    qjmc: Optional[str] = Query(None, description="区间名称"),
    dgjbh: Optional[str] = Query(None, description="盾构机编号"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    """获取盾构日报表数据（支持多条件筛选、分页）"""
    
    # 构建查询条件
    filters = Q()
    if id is not None:
        filters &= Q(id=id)
    if areaId is not None:
        filters &= Q(areaId=areaId)
    if qjmc is not None:
        filters &= Q(qjmc=qjmc)
    if dgjbh is not None:
        filters &= Q(dgjbh=dgjbh)

    # 获取总记录数
    total = await daily_paper.filter(filters).count()

    # 分页查询数据
    items = await daily_paper.filter(filters)\
        .offset((page - 1) * per_page)\
        .limit(per_page)\
        .order_by("-time")\
 
    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": [{
                "id": item.id,
                "areaId": item.areaId,
                "ljsh": item.ljsh,
                "dpnj": item.dpnj,
                "jjbz": item.jjbz,
                "cjll": item.cjll,
                "dpzs": item.dpzs,
                "kslc": item.kslc,
                "qjcd": item.qjcd,
                "tjsd": item.tjsd,
                "jjll": item.jjll,
                "cjbz": item.cjbz,
                "jrjd": item.jrjd,
                "ztl": item.ztl,
                "qjyl": item.qjyl,
                "grd": item.grd,
                "wcd": item.wcd,
                "qkyl": item.qkyl,
                "qpcyl": item.qpcyl,
                "qjmc": item.qjmc,
                "dgjbh": item.dgjbh,
                "pjrjc": item.pjrjc,
                "jslc": item.jslc,
                "sfsj": item.sfsj,
                "time": item.time,
            } for item in items],
            "total": total,
            "page": page,
            "per_page": per_page
        }
    }

@daily_paper_api.post("/update_daily_paper")
async def update_daily_paper(paper_data: DailyPaperUpdateModel):
    """更新日报表数据"""
    try:
        paper = await daily_paper.get_or_none(id=paper_data.id)
        if not paper:
            return {"status": 1, "msg": f"未找到ID为{paper_data.id}的记录"}
        
        await paper.update_from_dict(paper_data.dict(exclude_unset=True))
        await paper.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@daily_paper_api.delete("/delete_daily_paper/{id}")
async def delete_daily_paper(id: int):
    """删除日报表数据"""
    try:
        paper = await daily_paper.get_or_none(id=id)
        if not paper:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await paper.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")


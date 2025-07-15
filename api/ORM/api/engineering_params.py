from fastapi import APIRouter, Query, HTTPException, Depends
from typing import Optional
from engineering_models import engineering_params
from tortoise.expressions import Q
from pydantic import BaseModel
from Rbac_utils import get_user_from_token, check_permission

engineering_params_api = APIRouter()

class engineeringparamsIn(BaseModel):
    instanceid: int
    sub_code: str
    pro_code: str
    pro_name: str
    max_diameter: Optional[int] = None
    rube_outerdiameter: Optional[int] = None
    rube_innerdiameter: Optional[int] = None
    rube_thick: Optional[int] = None
    rube_width: Optional[int] = None
    geocondition: Optional[str] = None
    remark: Optional[str] = None

@engineering_params_api.post("/engineering_params")
async def add_engineering_params(params_in: engineeringparamsIn):
    try:
        new_params = await engineering_params.create(**params_in.dict(exclude_unset=True))
        return {"status": 0, "msg": "添加成功", "data": {"id": new_params.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建工程参数失败: {str(e)}")

@engineering_params_api.get("/engineering_params_list")
async def get_engineering_params_list(
    id: Optional[int] = Query(None, description="编号"),
    instanceid: Optional[int] = Query(None, description="流程id"),
    sub_code: Optional[str] = Query(None, description="工点编码"),
    pro_code: Optional[str] = Query(None, description="项目编码"),
    pro_name: Optional[str] = Query(None, description="项目名称"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    """获取工程参数数据（支持按多个字段筛选、分页）"""
    
    # 构建查询条件
    filters = Q()
    if id is not None:
        filters &= Q(id=id)
    if instanceid is not None:
        filters &= Q(instanceid=instanceid)
    if sub_code:
        filters &= Q(sub_code=sub_code)
    if pro_code:
        filters &= Q(pro_code=pro_code)
    if pro_name:
        filters &= Q(pro_name=pro_name)

    # 获取总记录数
    total = await engineering_params.filter(filters).count()

    # 分页查询数据
    items = await engineering_params.filter(filters)\
        .offset((page - 1) * per_page)\
        .limit(per_page)

    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": [{
                "id": item.id,
                "instanceid": item.instanceid,
                "sub_code": item.sub_code,
                "pro_code": item.pro_code,
                "pro_name": item.pro_name,
                "max_diameter": item.max_diameter,
                "rube_outerdiameter": item.rube_outerdiameter,
                "rube_innerdiameter": item.rube_innerdiameter,
                "rube_thick": item.rube_thick,
                "rube_width": item.rube_width,
                "geocondition": item.geocondition,
                "remark": item.remark
            } for item in items],
            "total": total,
            "page": page,
            "per_page": per_page
        }
    }

class EngineeringParamsUpdateModel(BaseModel):
    id: int
    instanceid: int
    sub_code: str
    pro_code: str
    pro_name: str
    max_diameter: Optional[int] = None
    rube_outerdiameter: Optional[int] = None
    rube_innerdiameter: Optional[int] = None
    rube_thick: Optional[int] = None
    rube_width: Optional[int] = None
    geocondition: Optional[str] = None
    remark: Optional[str] = None

@engineering_params_api.post("/update_engineering_params")
async def update_engineering_params(params_data: EngineeringParamsUpdateModel):
    """更新工程参数数据"""
    try:
        params = await engineering_params.get_or_none(id=params_data.id)
        if not params:
            return {"status": 1, "msg": f"未找到ID为{params_data.id}的记录"}
        
        await params.update_from_dict(params_data.dict(exclude_unset=True))
        await params.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@engineering_params_api.delete("/delete_engineering_params/{id}")
async def delete_engineering_params(id: int):
    """删除工程参数数据"""
    try:
        params = await engineering_params.get_or_none(id=id)
        if not params:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await params.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
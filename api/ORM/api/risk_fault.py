from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from risk_fault_models import risk_fault_records
from tortoise.expressions import Q
from pydantic import BaseModel

risk_fault_api = APIRouter()

class riskfaultIn(BaseModel):
    connect_key: str
    ring: int
    sub_code: str
    sub_name: str
    risk_start_end_ring: Optional[str] = None
    risk_type: Optional[str] = None
    risk_content: Optional[str] = None
    risk_level: Optional[str] = None
    risk_desc: Optional[str] = None
    risk_prevention: Optional[str] = None
    risk_treatment: Optional[str] = None
    risk_impact: Optional[str] = None
    risk_early_warning: Optional[str] = None
    risk_early_warning_value: Optional[str] = None
    risk_monitoring_frequency: Optional[str] = None
    surface_settlement_monitoring_value: Optional[str] = None
    structure_deformation_value: Optional[str] = None
    alarm_ring_section: Optional[str] = None
    alarm_type: Optional[str] = None
    fault_occurrence_time: Optional[str] = None
    specific_fault_equipment: Optional[str] = None
    fault_type: Optional[str] = None
    fault_treatment_measures: Optional[str] = None
    sg_fssj: Optional[str] = None
    sg_yy: Optional[str] = None
    cl_jg: Optional[str] = None
    wx_yy: Optional[str] = None
    wx_nr: Optional[str] = None
    
@risk_fault_api.post("/risk_fault")
async def add_risk_fault(info_in: riskfaultIn):
    try:
        new_info = await risk_fault_records.create(**info_in.dict(exclude_unset=True))
        return {"status": 0, "msg": "添加成功", "data": {"id": new_info.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"添加失败: {str(e)}")

@risk_fault_api.get("/risk_fault_list")
async def get_risk_fault_list(
    id: Optional[int] = Query(None, description="编号"),
    sub_code: Optional[str] = Query(None, description="施工区间编码"),
    sub_name: Optional[str] = Query(None, description="施工区间名称"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    filters = Q()
    if id is not None:
        filters &= Q(id=id)
    if sub_code:
        filters &= Q(sub_code=sub_code)
    if sub_name:
        filters &= Q(sub_name=sub_name)

    total = await risk_fault_records.filter(filters).count()
    items = await risk_fault_records.filter(filters).offset((page - 1) * per_page).limit(per_page).all()
    
    # 将数据库对象转换为字典列表
    items_dict = [{
        'id': item.id,
        'connect_key': item.connect_key,
        'ring': item.ring,
        'sub_code': item.sub_code,
        'sub_name': item.sub_name,
        'risk_start_end_ring': item.risk_start_end_ring,
        'risk_type': item.risk_type,
        'risk_content': item.risk_content,
        'risk_level': item.risk_level,
        'risk_desc': item.risk_desc,
        'risk_prevention': item.risk_prevention,
        'risk_treatment': item.risk_treatment,
        'risk_impact': item.risk_impact,
        'risk_early_warning': item.risk_early_warning,
        'risk_early_warning_value': item.risk_early_warning_value,
        'risk_monitoring_frequency': item.risk_monitoring_frequency,
        'surface_settlement_monitoring_value': item.surface_settlement_monitoring_value,
        'structure_deformation_value': item.structure_deformation_value,
        'alarm_ring_section': item.alarm_ring_section,
        'alarm_type': item.alarm_type,
        'fault_occurrence_time': item.fault_occurrence_time,
        'specific_fault_equipment': item.specific_fault_equipment,
        'fault_type': item.fault_type,
        'fault_treatment_measures': item.fault_treatment_measures,
        'sg_fssj': item.sg_fssj,
        'sg_yy': item.sg_yy,
        'cl_jg': item.cl_jg,
        'wx_yy': item.wx_yy,
        'wx_nr': item.wx_nr
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

class riskfaultUpdateModel(BaseModel):
    id: int
    connect_key: str
    ring: int
    sub_code: str
    sub_name: str
    risk_start_end_ring: Optional[str] = None
    risk_type: Optional[str] = None
    risk_content: Optional[str] = None
    risk_level: Optional[str] = None
    risk_desc: Optional[str] = None
    risk_prevention: Optional[str] = None
    risk_treatment: Optional[str] = None
    risk_impact: Optional[str] = None
    risk_early_warning: Optional[str] = None
    risk_early_warning_value: Optional[str] = None
    risk_monitoring_frequency: Optional[str] = None
    surface_settlement_monitoring_value: Optional[str] = None
    structure_deformation_value: Optional[str] = None
    alarm_ring_section: Optional[str] = None
    alarm_type: Optional[str] = None
    fault_occurrence_time: Optional[str] = None
    specific_fault_equipment: Optional[str] = None
    fault_type: Optional[str] = None
    fault_treatment_measures: Optional[str] = None
    sg_fssj: Optional[str] = None
    sg_yy: Optional[str] = None
    cl_jg: Optional[str] = None
    wx_yy: Optional[str] = None
    wx_nr: Optional[str] = None

@risk_fault_api.post("/update_risk_fault")
async def update_risk_fault(info_data: riskfaultUpdateModel):
    try:
        info = await risk_fault_records.get_or_none(id=info_data.id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{info_data.id}的记录"}
        
        await info.update_from_dict(info_data.dict(exclude_unset=True))
        await info.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@risk_fault_api.delete("/delete_risk_fault/{id}")
async def delete_risk_fault(id: int):
    try:
        info = await risk_fault_records.get_or_none(id=id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await info.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
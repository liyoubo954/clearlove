from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from tunneling_instruction_models import Tunneling_Instruction_Table
from tortoise.expressions import Q
from pydantic import BaseModel

tunneling_instruction_api = APIRouter()

class TunnelingInstructionIn(BaseModel):
    project_code: str
    project_name: str
    ring_number: Optional[int] = None
    cutting_face_mileage: Optional[str] = None
    cover_thickness: Optional[float] = None
    notch_water_pressure: Optional[float] = None
    total_thrust: Optional[str] = None
    total_torque: Optional[str] = None
    tunneling_speed: Optional[str] = None
    cutterhead_speed: Optional[float] = None
    slurry_ratio: Optional[str] = None
    slurry_flow: Optional[str] = None
    sync_grouting_pressure_1: Optional[float] = None
    sync_grouting_volume_1: Optional[float] = None
    sync_grouting_pressure_2: Optional[float] = None
    sync_grouting_volume_2: Optional[float] = None
    sync_grouting_pressure_3: Optional[float] = None
    sync_grouting_volume_3: Optional[float] = None
    sync_grouting_pressure_4: Optional[float] = None
    sync_grouting_volume_4: Optional[float] = None
    sync_grouting_pressure_5: Optional[float] = None
    sync_grouting_volume_5: Optional[float] = None
    sync_grouting_pressure_6: Optional[float] = None
    sync_grouting_volume_6: Optional[float] = None
    excel_path: Optional[str] = None

class TunnelingInstructionUpdateIn(BaseModel):
    id: int
    project_code: str
    project_name: str
    ring_number: Optional[int] = None
    cutting_face_mileage: Optional[str] = None
    cover_thickness: Optional[float] = None
    notch_water_pressure: Optional[float] = None
    total_thrust: Optional[str] = None
    total_torque: Optional[str] = None
    tunneling_speed: Optional[str] = None
    cutterhead_speed: Optional[float] = None
    slurry_ratio: Optional[str] = None
    slurry_flow: Optional[str] = None
    sync_grouting_pressure_1: Optional[float] = None
    sync_grouting_volume_1: Optional[float] = None
    sync_grouting_pressure_2: Optional[float] = None
    sync_grouting_volume_2: Optional[float] = None
    sync_grouting_pressure_3: Optional[float] = None
    sync_grouting_volume_3: Optional[float] = None
    sync_grouting_pressure_4: Optional[float] = None
    sync_grouting_volume_4: Optional[float] = None
    sync_grouting_pressure_5: Optional[float] = None
    sync_grouting_volume_5: Optional[float] = None
    sync_grouting_pressure_6: Optional[float] = None
    sync_grouting_volume_6: Optional[float] = None
    excel_path: Optional[str] = None

@tunneling_instruction_api.post("/tunneling_instruction")
async def add_tunneling_instruction(info_in: TunnelingInstructionIn):
    try:
        new_info = await Tunneling_Instruction_Table.create(**info_in.dict(exclude_unset=True))
        return {"status": 0, "msg": "添加成功", "data": {"id": new_info.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"添加失败: {str(e)}")

@tunneling_instruction_api.get("/tunneling_instruction_list")
async def get_tunneling_instruction_list(
    id: Optional[int] = Query(None, description="编号"),
    project_code: Optional[str] = Query(None, description="盾构机编号"),
    project_name: Optional[str] = Query(None, description="项目名称"),
    ring_number: Optional[int] = Query(None, description="环号"),
    page: int = Query(1, ge=1, description="页码"),
    per_page: int = Query(10, ge=1, le=100, description="每页数量")
):
    filters = Q()
    if id is not None:
        filters &= Q(id=id)
    if project_code:
        filters &= Q(project_code=project_code)
    if project_name:
        filters &= Q(project_name=project_name)
    if ring_number is not None:
        filters &= Q(ring_number=ring_number)

    total = await Tunneling_Instruction_Table.filter(filters).count()
    offset = (page - 1) * per_page
    items = await Tunneling_Instruction_Table.filter(filters).offset(offset).limit(per_page).all()
    
    return {
        "status": 0,
        "msg": "",
        "data": {
            "items": items,
            "total": total
        }
    }

@tunneling_instruction_api.post("/update_tunneling_instruction")
async def update_tunneling_instruction(info_in: TunnelingInstructionUpdateIn):
    try:
        info = await Tunneling_Instruction_Table.get_or_none(id=info_in.id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{info_in.id}的记录"}
        
        await info.update_from_dict(info_in.dict(exclude_unset=True))
        await info.save()
        return {"status": 0, "msg": "更新成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

@tunneling_instruction_api.delete("/delete_tunneling_instruction/{id}")
async def delete_tunneling_instruction(id: int):
    try:
        info = await Tunneling_Instruction_Table.get_or_none(id=id)
        if not info:
            return {"status": 1, "msg": f"未找到ID为{id}的记录"}
        
        await info.delete()
        return {"status": 0, "msg": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {str(e)}")
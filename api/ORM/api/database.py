from fastapi import APIRouter, Query, HTTPException, Body, Depends
from fastapi.responses import FileResponse
from tortoise.expressions import Q
from typing import Optional, Dict, Any
from datetime import datetime
from ddg_models import bar_chart_report
from pydantic import BaseModel
from Rbac_utils import get_user_from_token, check_permission
import pandas as pd
import os

database_api = APIRouter()

@database_api.get("/bar_chart_report")
async def get_project_report_list(
    sub_name: Optional[str] = Query(None, description="项目名称"),
    sub_code: Optional[str] = Query(None, description="项目编码"),
    type: Optional[int] = Query(None, description="项目类型"),
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100)
):
    """获取盾构项目报表数据（支持项目名称筛选、分页）"""
    filters = Q()
    if sub_name:
        filters &= Q(sub_name__icontains=sub_name)
    if sub_code:
        filters &= Q(sub_code__icontains=sub_code)
    if type is not None:
        filters &= Q(type=type)

    total = await bar_chart_report.filter(filters).count()
    items = await bar_chart_report.filter(filters) \
        .offset((page - 1) * per_page) \
        .limit(per_page) \
        .order_by("-time")

    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": [{
                "id": item.id,
                "sub_code": item.sub_code,
                "sub_name": item.sub_name,
                "type": item.type,
                "connect_key": item.connect_key,
                "take_time": item.take_time,
                "time": item.time,
                "driver": item.driver,
                "foreman": item.foreman,
                "assembler": item.assembler,
                "work_time": item.work_time,
                "fault_time": item.fault_time,
            } for item in items],
            "total": total,
            "page": page,
            "per_page": per_page
        }
    }


class ReportUpdateModel(BaseModel):
    id: int
    sub_code: str
    sub_name: str
    type: int
    connect_key: str
    driver: Optional[str] = None
    foreman: Optional[str] = None
    assembler: Optional[str] = None


@database_api.post("/update_report")
async def update_report(report_data: ReportUpdateModel):
    """更新盾构项目报表数据"""
    try:
        # 检查记录是否存在
        report = await bar_chart_report.get_or_none(id=report_data.id)
        if not report:
            return {
                "status": 1,
                "msg": f"未找到ID为{report_data.id}的记录"
            }
        
        # 更新记录
        report.sub_code = report_data.sub_code
        report.sub_name = report_data.sub_name
        report.type = report_data.type
        report.connect_key = report_data.connect_key
        report.driver = report_data.driver
        report.foreman = report_data.foreman
        report.assembler = report_data.assembler
        
        await report.save()
        
        return {
            "status": 0,
            "msg": "更新成功"
        }
    except Exception as e:
        return {
            "status": 1,
            "msg": f"更新失败: {str(e)}"
        }


@database_api.delete("/delete_report")
async def delete_report(id: int):
    """删除盾构项目报表数据"""
    try:
        # 检查记录是否存在
        report = await bar_chart_report.get_or_none(id=id)
        if not report:
            return {
                "status": 1,
                "msg": f"未找到ID为{id}的记录"
            }
        
        # 删除记录
        await report.delete()
        
        return {
            "status": 0,
            "msg": "删除成功"
        }
    except Exception as e:
        return {
            "status": 1,
            "msg": f"删除失败: {str(e)}"
        }

@database_api.get("/export_excel")
async def export_excel(
    sub_name: Optional[str] = Query(None, description="项目名称"),
    sub_code: Optional[str] = Query(None, description="项目编码"),
    type: Optional[int] = Query(None, description="项目类型")
):
    """
    导出项目报表数据为Excel
    """
    # 检查导出权限
    await check_permission(user, "project:export")
    
    filters = Q()
    if sub_name:
        filters &= Q(sub_name__icontains=sub_name)
    if sub_code:
        filters &= Q(sub_code__icontains=sub_code)
    if type is not None:
        filters &= Q(type=type)

    # 获取所有符合条件的数据
    items = await bar_chart_report.filter(filters).all()
    
    # 转换为DataFrame
    data = [{
        "项目编号": item.sub_code,
        "项目名称": item.sub_name,
        "项目类型": item.type,
        "连接密钥": item.connect_key,
        "施工时间": item.take_time,
        "记录时间": item.time,
        "司机": item.driver,
        "工长": item.foreman,
        "装配工": item.assembler,
        "工作时间": item.work_time,
        "故障时间": item.fault_time
    } for item in items]
    
    df = pd.DataFrame(data)
    
    # 确保导出目录存在
    export_dir = "exports"
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
    
    # 生成文件名
    filename = f"项目报表_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    file_path = os.path.join(export_dir, filename)
    
    # 保存为Excel文件
    df.to_excel(file_path, index=False)
    
    # 返回文件
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

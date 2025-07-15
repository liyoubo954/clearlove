from fastapi import FastAPI, Request, HTTPException, Depends
import uvicorn
import os
from tortoise.contrib.fastapi import register_tortoise
from api.adminuser import adminuser_api
from api.get_file import file_api
from api.database import database_api
from api.daily_paper import  daily_paper_api
from api.engineering_params import engineering_params_api
from api.segment_info import segment_info_api
from api.project_stats import project_stats_api
from api.main_drive import main_drive_api
from api.risk_fault import risk_fault_api
from api.shield_machine import shield_machine_api
from api.shield_info import shield_info_api
from api.construction_progress import construction_progress_api
from api.geology_data import geology_data_api
from api.disk_info import disk_info_api  
from api.remote_file import remote_file_api
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
from api.tunneling_instruction import tunneling_instruction_api
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from settings import TORTOISE_ORM
from init_rbac import init_rbac  # 导入你的初始化函数

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动时调用初始化函数
    await init_rbac()
    yield
    # 应用关闭时的清理代码（如果需要）
    pass

# 定义一个依赖函数，用于检查请求是否来自本地
async def check_local_access(request: Request):
    host = request.client.host
    if host != "127.0.0.1" and host != "localhost":
        raise HTTPException(status_code=403, detail="API文档只允许本地访问")
    return True

# 创建 FastAPI 应用实例
app = FastAPI(
    lifespan=lifespan,
    title="盾构管理系统API",
    description="盾构管理系统的后端API接口文档",
    version="1.0.0",
    # 不直接设置docs_url和redoc_url，我们将手动添加这些路由
    docs_url=None,
    redoc_url=None
)

# CORS 配置
# 允许所有域名访问，包括API文档
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源
    allow_credentials=False,  # 不使用credentials
    allow_methods=["*"],
    allow_headers=["*"],
)

# 直接指定项目根目录路径
PROJECT_ROOT = "d:\\APP\\GItHub"
# 挂载静态资源目录
app.mount("/pages", StaticFiles(directory=os.path.join(PROJECT_ROOT, "pages")), name="pages")
app.mount("/sdk", StaticFiles(directory=os.path.join(PROJECT_ROOT, "sdk")), name="sdk")
app.mount("/amis", StaticFiles(directory=os.path.join(PROJECT_ROOT, "amis")), name="amis")

# 根路径处理，返回login.html
@app.get("/")
async def read_root():
    return FileResponse(os.path.join(PROJECT_ROOT, "login.html"))

# 登录页面路由
@app.get("/login.html")
async def read_login():
    return FileResponse(os.path.join(PROJECT_ROOT, "login.html"))

# 主页路由
@app.get("/index.html")
async def read_index():
    return FileResponse(os.path.join(PROJECT_ROOT, "index.html"))

# 添加favicon.ico路由
@app.get("/favicon.ico")
async def get_favicon():
    return FileResponse(os.path.join(PROJECT_ROOT, "favicon.ico"), media_type="image/x-icon")

# 手动添加API文档路由，仅允许本地访问
@app.get("/docs", dependencies=[Depends(check_local_access)])
async def get_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json", title=app.title + " - Swagger UI")

@app.get("/redoc", dependencies=[Depends(check_local_access)])
async def get_redoc():
    return get_redoc_html(openapi_url="/openapi.json", title=app.title + " - ReDoc")

@app.get("/openapi.json", dependencies=[Depends(check_local_access)])
async def get_openapi_json():
    return get_openapi(title=app.title, version=app.version, description=app.description, routes=app.routes)

# 注册路由
app.include_router(adminuser_api, prefix="/adminuser", tags=["管理员用户"])
app.include_router(file_api, prefix="/file", tags=["上传文件"])
app.include_router(database_api, prefix="/bar_chart", tags=["项目报表"])
app.include_router(daily_paper_api,prefix="/daily_paper",tags=["日报表"])
app.include_router(engineering_params_api, prefix="/engineering_params", tags=["工程参数"])
app.include_router(segment_info_api, prefix="/segment_info", tags=["管片信息"])
app.include_router(project_stats_api, prefix="/project_stats", tags=["大盾构项目统计"])
app.include_router(main_drive_api, prefix="/main_drive", tags=["主驱动运行时间统计"]) 
app.include_router(risk_fault_api, prefix="/risk_fault", tags=["风险与故障记录"])
app.include_router(shield_machine_api, prefix="/shield_machine", tags=["盾构机基本信息"])
app.include_router(shield_info_api, prefix="/shield_info", tags=["掘进参数表"])
app.include_router(construction_progress_api, prefix="/construction_progress", tags=["施工进度报表"])
app.include_router(geology_data_api, prefix="/geology_data", tags=["地质数据表"])
app.include_router(disk_info_api, prefix="/disk_info", tags=["刀盘信息表"]) 
app.include_router(remote_file_api, prefix="/remote_file", tags=["minio文件"]) 
app.include_router(tunneling_instruction_api, prefix="/tunneling_instruction", tags=["盾构掘进指令表"])
# 注册 Tortoise ORM
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # 启用自动生成数据库表
    add_exception_handlers=True,
)


if __name__ == '__main__':
    # 使用0.0.0.0作为主机地址，这样可以同时接受来自本地和外部的连接
    # 本地用户仍然可以通过127.0.0.1:8010访问
    # 外部用户可以通过服务器的实际IP地址访问
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)

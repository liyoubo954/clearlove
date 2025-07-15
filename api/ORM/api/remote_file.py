from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel
import paramiko
import os
import stat

remote_file_api = APIRouter()

# 远程服务器配置
REMOTE_HOST = "172.16.105.12"
REMOTE_USERNAME = "ddg"  # 替换为实际用户名
REMOTE_PASSWORD = "zp123!@#"  # 替换为实际密码
REMOTE_BASE_PATH = "/data_sdd2/minio/minio_data"  # 远程服务器上的基础路径

class FileInfo(BaseModel):
    name: str
    size: int
    is_dir: bool
    last_modified: str
    path: str

@remote_file_api.get("/list_projects")
async def list_projects(project_name: Optional[str] = Query(None, description="项目名称")) -> List[str]:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(REMOTE_HOST, username=REMOTE_USERNAME, password=REMOTE_PASSWORD)
        sftp = ssh.open_sftp()
        
        # 获取项目列表
        projects = sftp.listdir(REMOTE_BASE_PATH)
        
        # 如果提供了项目名称参数，进行过滤
        if project_name:
            # 项目名称映射表（与前端保持一致）
            project_name_map = {
                'tongsujiayong': '通苏嘉甬',
                'shanghaijichanglianluoxian': '上海机场联络线',
                'suzhous1': '苏州S1',
                'qinwangtongdao': '秦望通道',
                'shenjiangtielu': '深江铁路',
                'shanshantielu': '汕汕铁路',
                'jingbintielu': '京滨铁路',
                'jingtangtielu': '京唐铁路',
                'xiangyalu': '湘雅路',
                'beijings6': '北京S6',
                'jianningxilu': '建宁西路'
            }
            
            # 创建反向映射表（中文名称 -> 英文项目名）
            reverse_map = {v: k for k, v in project_name_map.items()}
            
            # 搜索逻辑：支持中文名称和英文名称搜索
            filtered_projects = []
            search_term = project_name.lower().strip()
            
            for project in projects:
                project_lower = project.lower()
                # 获取项目的中文名称
                chinese_name = project_name_map.get(project_lower, project)
                
                # 检查是否匹配：
                # 1. 英文项目名包含搜索词
                # 2. 中文名称包含搜索词
                # 3. 搜索词是中文名称，反向查找英文名称
                if (search_term in project_lower or 
                    project_name in chinese_name or 
                    (project_name in reverse_map and reverse_map[project_name] == project_lower)):
                    filtered_projects.append(project)
            
            projects = filtered_projects
        
        return projects
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if 'sftp' in locals():
            sftp.close()
        if 'ssh' in locals():
            ssh.close()

@remote_file_api.get("/list_project_files")
async def list_project_files(project_name: str, sub_path: str = "") -> List[FileInfo]:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(REMOTE_HOST, username=REMOTE_USERNAME, password=REMOTE_PASSWORD)
        sftp = ssh.open_sftp()
        
        # 构建完整路径
        full_path = os.path.join(REMOTE_BASE_PATH, project_name, sub_path).replace("\\", "/")
        
        # 检查路径是否存在
        try:
            sftp.stat(full_path)
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"Path {full_path} not found.")
        
        # 获取文件列表
        file_list = []
        for entry in sftp.listdir_attr(full_path):
            file_path = os.path.join(sub_path, entry.filename).replace("\\", "/")
            
            # 基于常见文件扩展名判断文件类型
            filename_lower = entry.filename.lower()
            
            # 定义常见的文件扩展名
            file_extensions = {
                '.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx',
                '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico',
                '.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.mp3', '.wav', '.flac',
                '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
                '.dwg', '.dxf', '.step', '.iges', '.stl',
                '.py', '.js', '.html', '.css', '.json', '.xml', '.csv',
                '.exe', '.msi', '.deb', '.rpm', '.dmg',
                '.log', '.ini', '.cfg', '.conf', '.yaml', '.yml','.bak'
            }
            
            # 检查文件名是否以已知的文件扩展名结尾
            is_file = any(filename_lower.endswith(ext) for ext in file_extensions)
            is_directory = not is_file
            
            file_info = FileInfo(
                name=entry.filename,
                size=entry.st_size,
                is_dir=is_directory,
                last_modified=str(entry.st_mtime),
                path=file_path
            )
            file_list.append(file_info)
        
        return file_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if 'sftp' in locals():
            sftp.close()
        if 'ssh' in locals():
            ssh.close()
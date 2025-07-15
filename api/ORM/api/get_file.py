from fastapi import APIRouter, UploadFile, Depends
from typing import List
import os
from Rbac_utils import get_user_from_token, check_permission

# 指定文件保存的目录
UPLOAD_DIR = "amis/file"

# 如果目录不存在，则创建它
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

file_api = APIRouter()

@file_api.post("/uploadfiles")  # 修改这里
async def get_file(file: List[UploadFile], user = Depends(get_user_from_token)):
    # 检查文件上传权限
    await check_permission(user, "file:upload")
    uploaded_files = []
    for fil in file:
        try:
            # 构建文件的完整保存路径
            file_path = os.path.join(UPLOAD_DIR, fil.filename)
            contents = await fil.read()
            with open(file_path, "wb") as f:
                f.write(contents)
            uploaded_files.append(file_path)
        except Exception as e:
            return {
                "status": 1,
                "msg": f"文件 {fil.filename} 上传失败: {str(e)}",
                "data": {}
            }
        finally:
            await fil.close()
    return {
        "status": 0,
        "msg": "文本上传成功",
        "data": {
            "values": uploaded_files
        }
    }
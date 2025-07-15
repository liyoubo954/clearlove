from fastapi import APIRouter, HTTPException, Request, Query, Depends, status
from fastapi.responses import FileResponse
from typing import Optional
from models import adminuser
from Rbac_utils import get_user_from_token, check_permission
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from tortoise.exceptions import DoesNotExist
from tortoise.expressions import Q
import pandas as pd
import os
from datetime import datetime

# OAuth2 token scheme，登录接口地址
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# JWT配置
SECRET_KEY = "your-secret-key"  # 生产环境应从环境变量获取
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 密码加密工具
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
adminuser_api = APIRouter()

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭证",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token已过期")
    except jwt.PyJWTError:
        raise credentials_exception
    
    user = await adminuser.get_or_none(username=username)
    if user is None:
        raise credentials_exception
    return user

# 请求模型
class LoginRequest(BaseModel):
    username: str
    password: str

class adminuserIn(BaseModel):
    username: str
    password: str
    phone: Optional[str] = None
    remark: Optional[str] = None

# 登录接口（使用JWT）
@adminuser_api.post("/login")
async def adminuser_login(login_request: LoginRequest):
    try:
        user = await adminuser.get(username=login_request.username)
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="该用户不存在")

    if not verify_password(login_request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户名或密码错误")

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {
        "code": 0,
        "msg": "登录成功",
        "data": {
            "access_token": access_token,
            "token_type": "bearer"
        }
    }

# 新增用户
@adminuser_api.post("/")
async def add_adminuser(adminuser_in: adminuserIn, user=Depends(get_current_user)):
    await check_permission(user, "adminuser:add")
    try:
        new_user = await adminuser.create(
            username=adminuser_in.username,
            password=hash_password(adminuser_in.password),
            phone=adminuser_in.phone,
            remark=adminuser_in.remark
        )
        return {"code": 0, "msg": "创建成功", "data": {"id": new_user.id}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建用户失败: {str(e)}")

# 获取分页用户列表
@adminuser_api.get("/page")
async def get_adminuser_page(page: int = Query(1, ge=1), perPage: int = Query(10, ge=1), username: Optional[str] = Query(None), phone: Optional[str] = Query(None), user=Depends(get_current_user)):
    await check_permission(user, "adminuser:view")
    offset = (page - 1) * perPage
    query = adminuser.all()
    if username:
        query = query.filter(username__icontains=username)
    if phone:
        query = query.filter(phone__icontains=phone)
    total = await query.count()
    users = await query.offset(offset).limit(perPage)
    return {
        "code": 0,
        "msg": "",
        "data": {
            "page": page,
            "perPage": perPage,
            "username": username,
            "items": [
                {
                    "id": u.id,
                    "username": u.username,
                    "password": u.password,
                    "phone": u.phone,
                    "remark": u.remark,
                    "createtime": u.createtime,
                    "updatetime": u.updatetime
                } for u in users
            ],
            "total": total
        }
    }

# 获取单个用户详情
@adminuser_api.get("/{id}")
async def get_adminuser_detail(id: int, user=Depends(get_current_user)):
    await check_permission(user, "adminuser:view")
    try:
        user_obj = await adminuser.get(id=id)
        return {
            "code": 0,
            "msg": "",
            "data": {
                "id": user_obj.id,
                "username": user_obj.username,
                "remark": user_obj.remark,
                "createtime": user_obj.createtime,
                "updatetime": user_obj.updatetime
            }
        }
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"用户 {id} 未找到")

# 删除用户
@adminuser_api.delete("/{id}")
async def del_adminuser(id: int, user=Depends(get_current_user)):
    await check_permission(user, "adminuser:delete")
    delete_count = await adminuser.filter(id=id).delete()
    if delete_count == 0:
        raise HTTPException(status_code=404, detail=f"用户 {id} 未找到")
    return {"code": 0, "msg": f"删除id为{id}的用户成功"}



# 更新用户
@adminuser_api.put("/{id}")
async def update_adminuser(id: int, adminuser_in: adminuserIn, user=Depends(get_current_user)):
    await check_permission(user, "adminuser:update")
    try:
        updated_count = await adminuser.filter(id=id).update(
            username=adminuser_in.username,
            password=hash_password(adminuser_in.password),
            phone=adminuser_in.phone,
            remark=adminuser_in.remark,
            updatetime=datetime.now(timezone.utc)
        )
        if updated_count == 0:
            raise HTTPException(status_code=404, detail="用户不存在")
        updated_user = await adminuser.get(id=id)
        return {
            "code": 0,
            "msg": "更新成功",
            "data": {
                "id": updated_user.id,
                "username": updated_user.username,
                "remark": updated_user.remark,
                "updatetime": updated_user.updatetime
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新失败: {str(e)}")

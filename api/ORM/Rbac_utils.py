from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from models import adminuser

# JWT配置（与adminuser.py保持一致）
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_user_from_token(token: str = Depends(oauth2_scheme)) -> adminuser:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Token中无用户名")

        user = await adminuser.get(username=username)
        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token已过期")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="无效Token")
    except adminuser.DoesNotExist:
        raise HTTPException(status_code=401, detail="无效用户")

async def check_permission(user: adminuser, perm_code: str):
    roles = await user.roles.all().prefetch_related("permissions")
    all_permissions = set()
    for role in roles:
        perms = await role.permissions.all()
        all_permissions.update(p.code for p in perms)
    if perm_code not in all_permissions:
        raise HTTPException(status_code=403, detail=f"权限被拒绝：{perm_code}")
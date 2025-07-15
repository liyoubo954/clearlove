# init_rbac.py
from models import role, permission, adminuser
import datetime

async def init_rbac():
    # ✅ 创建权限项
    perms_data = [
        ("用户查看", "adminuser:view"),
        ("用户新增", "adminuser:add"),
        ("用户修改", "adminuser:update"),
        ("用户删除", "adminuser:delete"),
        ("文件上传", "file:upload"),
        ("项目查看", "project:view"),
        ("项目查询", "project:search"),
        ("项目修改", "project:update"),
        ("项目删除", "project:delete"),
        ("导出Excel", "project:export")
    ]
    for name, code in perms_data:
        await permission.get_or_create(code=code, defaults={"name": name})

    # ✅ 创建角色
    admin_role, _ = await role.get_or_create(name="管理员")
    manager_role, _ = await role.get_or_create(name="项目负责人")
    normal_role, _ = await role.get_or_create(name="普通用户")

    # ✅ 角色分配权限
    all_perms = await permission.all()
    # 管理员拥有所有权限
    await admin_role.permissions.add(*all_perms)
    
    # 项目负责人权限
    await manager_role.permissions.clear()
    await manager_role.permissions.add(
        await permission.get(code="adminuser:view"),
        await permission.get(code="file:upload"),
        await permission.get(code="project:view"),
        await permission.get(code="project:search")
    )
    
    # 普通用户权限
    await normal_role.permissions.clear()
    await normal_role.permissions.add(
        await permission.get(code="adminuser:view"),
        await permission.get(code="project:view")
    )

    # ✅ 用户角色分配
    admins = ["admin"]
    managers = ["curry"]
    normals = ["clearlove"]

    for username in admins:
        user = await adminuser.get(username=username)
        await user.roles.clear()
        await user.roles.add(admin_role)

    for username in managers:
        user = await adminuser.get(username=username)
        await user.roles.clear()
        await user.roles.add(manager_role)

    for username in normals:
        user = await adminuser.get(username=username)
        await user.roles.clear()
        await user.roles.add(normal_role)

    return {"message": "RBAC 初始化完成"}


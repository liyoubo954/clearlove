# models.py
from tortoise.models import Model
from tortoise import fields

class adminuser(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, description="用户名", null=True)
    password = fields.CharField(max_length=255, description="密码", null=True)
    phone = fields.CharField(max_length=20, description="电话", null=True)
    remark = fields.CharField(max_length=255, description="备注", null=True)
    createtime = fields.DatetimeField(auto_now_add=True, description="创建时间", null=True)
    updatetime = fields.DatetimeField(auto_now=True, description="更新时间", null=True)

    roles: fields.ManyToManyRelation["role"]  # 声明反向引用

class role(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, unique=True, description="角色名称", null=True)
    description = fields.CharField(max_length=255, null=True, description="角色描述")
    users = fields.ManyToManyField(
        "models.adminuser",
        related_name="roles",
        through="admin_role"
    )
    permissions: fields.ManyToManyRelation["permission"]

class permission(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, unique=True, description="权限名称", null=True)
    code = fields.CharField(max_length=64, unique=True, description="权限代码", null=True)
    description = fields.CharField(max_length=255, null=True, description="权限描述")
    roles = fields.ManyToManyField(
        "models.role",
        related_name="permissions",
        through="role_permission"
    )

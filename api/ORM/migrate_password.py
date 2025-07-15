import sys
import os
import asyncio
from tortoise import Tortoise, run_async
from passlib.context import CryptContext

# 添加项目路径，确保能找到 models
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from models import adminuser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def reset_all_passwords():
    await Tortoise.init(
        db_url='mysql://root:lyb5201314@localhost:3306/fastapi',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

    new_password = "123456"
    users = await adminuser.all()
    for user in users:
        user.password = pwd_context.hash(new_password)
        await user.save()
        print(f"✅ 用户 {user.username} 密码已重置为 {new_password}")

    print(f"🎉 共重置 {len(users)} 个用户密码")
    await Tortoise.close_connections()

if __name__ == "__main__":
    run_async(reset_all_passwords())

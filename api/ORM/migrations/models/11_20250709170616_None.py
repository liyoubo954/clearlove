from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `adminuser` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(255) COMMENT '用户名',
    `password` VARCHAR(255) COMMENT '密码',
    `phone` VARCHAR(20) COMMENT '电话',
    `remark` VARCHAR(255) COMMENT '备注',
    `createtime` DATETIME(6) COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updatetime` DATETIME(6) COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `permission` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) UNIQUE COMMENT '权限名称',
    `code` VARCHAR(64) UNIQUE COMMENT '权限代码',
    `description` VARCHAR(255) COMMENT '权限描述'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `role` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) UNIQUE COMMENT '角色名称',
    `description` VARCHAR(255) COMMENT '角色描述'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `role_permission` (
    `permission_id` INT NOT NULL,
    `role_id` INT NOT NULL,
    FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_role_permis_permiss_b3cd23` (`permission_id`, `role_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `admin_role` (
    `role_id` INT NOT NULL,
    `adminuser_id` INT NOT NULL,
    FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`adminuser_id`) REFERENCES `adminuser` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_admin_role_role_id_eeabca` (`role_id`, `adminuser_id`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """

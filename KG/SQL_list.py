import pymysql

# 数据库连接信息
host = '172.16.105.12'
user = 'root'
password = '123456'
database = 'zstp'
port = 13366

# 连接数据库
conn = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    port=port,
    charset='utf8mb4'
)
cursor = conn.cursor()

# 创建 entity_types 实体类型表
cursor.execute("""
CREATE TABLE IF NOT EXISTS entity_types (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '实体类型的唯一id',
    Etype_name VARCHAR(255) COMMENT '实体类型的名称'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")

# 创建 entities 实体表 (已加入“先验概率”字段)
# The `entities` table creation statement has been updated to include the prior_probability field.
cursor.execute("""
CREATE TABLE IF NOT EXISTS entities (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '实体的唯一id',
    etype_id INT COMMENT '实体类型的ID，外键关联entity_types表',
    name VARCHAR(255) COMMENT '实体内容',
    attributes JSON COMMENT '实体属性内容',
    prior_probability FLOAT COMMENT '先验概率',
    FOREIGN KEY (etype_id) REFERENCES entity_types(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")

# 创建 relationship_types 关系类型表
cursor.execute("""
CREATE TABLE IF NOT EXISTS relationship_types (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '关系类型的唯一id',
    Rtype_name VARCHAR(255) COMMENT '关系类型的名称'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")

# 创建 triple 三元组表
cursor.execute("""
CREATE TABLE IF NOT EXISTS triple (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '三元组唯一id',
    subject_id INT COMMENT '首实体的ID（关系的起点）',
    relationship_id INT COMMENT '关系类型id',
    object_id INT COMMENT '尾部实体的ID（关系的终点）',
    FOREIGN KEY (subject_id) REFERENCES entities(id),
    FOREIGN KEY (relationship_id) REFERENCES relationship_types(id),
    FOREIGN KEY (object_id) REFERENCES entities(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")

print("所有表已创建完成！")

# 关闭连接
cursor.close()
conn.close()
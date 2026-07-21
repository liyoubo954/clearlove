import pymysql
import pandas as pd
from sqlalchemy import create_engine
import json

# --- 配置区 ---
# 数据库连接配置信息
host = '172.16.105.12'
user = 'root'
password = '123456'
database = 'zstp'
port = 13366

# Excel文件中的列名，请确保与你的文件完全一致
ENTITY_TYPE_COL = '实体类型'
ENTITY_NAME_COL = '实体名称'
ENTITY_DESC_COL = '描述'
ENTITY_PROB_COL = '概率'  # 先验概率列的标题

REL_SUBJECT_COL = '首实体'
REL_RELATION_COL = '关系'
REL_OBJECT_COL = '尾实体'

# --- 代码区 ---

# 创建数据库连接
try:
    conn = pymysql.connect(
        host=host, user=user, password=password, database=database,
        port=port, charset='utf8mb4'
    )
    cursor = conn.cursor()
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
except Exception as e:
    print(f"数据库连接失败: {e}")
    exit()


def import_entity_types_and_entities(entity_file):
    """
    导入实体类型和实体数据到数据库 (已更新)
    """
    try:
        # 读取Excel，默认第一行为表头
        df = pd.read_excel(entity_file)
        # 删除完全是空的行
        df.dropna(how='all', inplace=True)
        # 清除关键列的前后空格
        df[ENTITY_TYPE_COL] = df[ENTITY_TYPE_COL].astype(str).str.strip()
        df[ENTITY_NAME_COL] = df[ENTITY_NAME_COL].astype(str).str.strip()

    except FileNotFoundError:
        print(f"错误: 实体文件未找到 -> {entity_file}")
        return
    except KeyError as e:
        print(f"错误: 实体文件中缺少必要的列: {e}。请检查列名是否与配置区一致。")
        return

    # 获取唯一的实体类型并插入数据库
    entity_types = df[ENTITY_TYPE_COL].unique()
    type_id_map = {}
    for etype in entity_types:
        if etype and etype != 'nan':
            cursor.execute("INSERT INTO entity_types (Etype_name) VALUES (%s)", (etype,))
            type_id_map[etype] = cursor.lastrowid

    # 遍历实体数据并插入数据库
    for _, row in df.iterrows():
        etype = row[ENTITY_TYPE_COL]
        name = row[ENTITY_NAME_COL]

        # 检查必填字段是否为空
        if not all([etype, name]) or etype == 'nan' or name == 'nan':
            print(f"跳过缺少类型或名称的行: {row.to_dict()}")
            continue

        # 处理实体描述
        attributes_json = None
        if ENTITY_DESC_COL in row and pd.notna(row[ENTITY_DESC_COL]):
            attributes_json = json.dumps({"description": str(row[ENTITY_DESC_COL])}, ensure_ascii=False)

        # 处理先验概率
        prior_probability = None
        if ENTITY_PROB_COL in row and pd.notna(row[ENTITY_PROB_COL]):
            try:
                prior_probability = float(row[ENTITY_PROB_COL])
            except (ValueError, TypeError):
                # 这个警告现在只会在数据行出现问题时触发，而不会在表头行
                print(f"警告: 无法转换概率值为浮点数 '{row[ENTITY_PROB_COL]}'。对于实体 '{name}'，将使用 NULL。")

        try:
            cursor.execute(
                "INSERT INTO entities (etype_id, name, attributes, prior_probability) VALUES (%s, %s, %s, %s)",
                (type_id_map.get(etype), name, attributes_json, prior_probability)
            )
        except Exception as e:
            print(f"插入实体 '{name}' 时出错: {e}")

    conn.commit()


def import_relationships(triple_file):
    """
    导入三元组关系数据到数据库 (已更新)
    """
    try:
        df = pd.read_excel(triple_file)
        df.dropna(how='all', inplace=True)
        # 清除所有关系列的前后空格
        df[REL_SUBJECT_COL] = df[REL_SUBJECT_COL].astype(str).str.strip()
        df[REL_RELATION_COL] = df[REL_RELATION_COL].astype(str).str.strip()
        df[REL_OBJECT_COL] = df[REL_OBJECT_COL].astype(str).str.strip()

    except FileNotFoundError:
        print(f"错误: 关系文件未找到 -> {triple_file}")
        return
    except KeyError as e:
        print(f"错误: 关系文件中缺少必要的列: {e}。请检查列名是否与配置区一致。")
        return

    # 获取并插入唯一的关系类型
    relationship_types = df[REL_RELATION_COL].unique()
    rel_type_id_map = {}
    for rtype in relationship_types:
        if rtype and rtype != 'nan':
            cursor.execute("INSERT INTO relationship_types (Rtype_name) VALUES (%s)", (rtype,))
            rel_type_id_map[rtype] = cursor.lastrowid

    # 获取所有实体的ID映射
    cursor.execute("SELECT id, name FROM entities")
    entity_map = {name: id for id, name in cursor.fetchall()}

    # 遍历三元组数据并插入
    for _, row in df.iterrows():
        subject = row[REL_SUBJECT_COL]
        relationship = row[REL_RELATION_COL]
        object_entity = row[REL_OBJECT_COL]

        if not all([subject, relationship,
                    object_entity]) or subject == 'nan' or relationship == 'nan' or object_entity == 'nan':
            continue

        subject_id = entity_map.get(subject)
        object_id = entity_map.get(object_entity)
        relationship_id = rel_type_id_map.get(relationship)

        if subject_id and object_id and relationship_id:
            cursor.execute(
                "INSERT INTO triple (subject_id, relationship_id, object_id) VALUES (%s, %s, %s)",
                (subject_id, relationship_id, object_id)
            )
        else:
            # 这个提示现在更精确地指明了问题所在
            print(f"跳过无效关系: {subject} -> {relationship} -> {object_entity}。原因: 实体或关系未在数据库中找到。")

    conn.commit()


def main():
    """
    主函数：协调整个数据导入过程
    """
    try:
        entity_file = "F:\\ddg\\KG\\最终_类型描述.xlsx"
        triple_file = "F:\\ddg\\KG\\最终_纯三元组.xlsx"

        print("开始清空旧数据...")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        cursor.execute("TRUNCATE TABLE triple;")
        cursor.execute("TRUNCATE TABLE entities;")
        cursor.execute("TRUNCATE TABLE entity_types;")
        cursor.execute("TRUNCATE TABLE relationship_types;")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        print("旧数据已清空。")

        print("\n开始导入实体类型和实体数据...")
        import_entity_types_and_entities(entity_file)
        print("实体数据导入完成！")

        print("\n开始导入关系数据...")
        import_relationships(triple_file)
        print("关系数据导入完成！")

    except Exception as e:
        print(f"\n导入过程中出现严重错误: {e}")
        conn.rollback()
    finally:
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()
            print("\n数据库连接已关闭。")


if __name__ == "__main__":
    main()
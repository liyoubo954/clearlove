import pandas as pd
from py2neo import Graph, NodeMatcher
import os

# 连接到Neo4j数据库
try:
    graph = Graph('bolt://localhost:7687', auth=("neo4j", "xty328310"))
    print("成功连接到Neo4j数据库。")
except Exception as e:
    print(f"连接到Neo4j数据库时发生错误: {e}")
    exit()

# 确认文件路径
#file_path = 'F:\\ddg\\KG\\图谱\\结泥饼类型描述.xlsx'
#file_path = 'F:\\ddg\\KG\\图谱\\滞排类型描述.xlsx'
#file_path = 'F:\\ddg\\KG\\图谱\\盾尾密封失效类型描述.xlsx'
#file_path = 'F:\\ddg\\KG\\图谱\\主轴承损坏类型描述.xlsx'
file_path = 'F:\ddg\KG\带压进仓_类型描述.xlsx'

if not os.path.exists(file_path):
    print(f"文件未找到: {file_path}")
    exit()

# 读取Excel文件（仅第一列是节点名称，第二列是实体标签）
try:
    data = pd.read_excel(file_path, usecols=[0, 1, 2], names=["name", "labels", "desc"])
    print("成功加载Excel文件。")
except Exception as e:
    print(f"加载Excel文件时发生错误: {e}")
    exit()

# 初始化 NodeMatcher
matcher = NodeMatcher(graph)

for index, row in data.iterrows():
    node_name = row["name"]
    labels_str = row["labels"]

    # 跳过空值
    if pd.isna(node_name) or pd.isna(labels_str):
        continue

    # 查询节点（确保匹配已有节点）
    node = matcher.match(name=node_name).first()
    if node:
        new_labels = {label.strip() for label in labels_str.split(',') if label.strip()}
        new_labels.discard('Entity')
        desc = None if pd.isna(row['desc']) else str(row['desc'])
        label_str = ':'.join(sorted(new_labels)) if new_labels else ''
        cypher = 'MATCH (n {name: $name}) REMOVE n:Entity SET n.描述 = $desc'
        if label_str:
            cypher += f' SET n:{label_str}'
        graph.run(cypher, name=node_name, desc=desc)
        print(f"已更新节点 '{node_name}' 的标签为 {new_labels}，描述更新为：{desc}。")
    else:
        print(f"未找到节点 '{node_name}'，跳过。")

print("节点标签更新完成。")
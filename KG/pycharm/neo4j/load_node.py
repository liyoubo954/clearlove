import pandas as pd
from py2neo import Graph, Node, Relationship, Subgraph
import os

# 连接到Neo4j数据库
try:
    graph = Graph('bolt://localhost:7687', auth=("neo4j", "xty328310"))
    graph.delete_all()  # 清空原有数据（根据需求决定是否保留）
    print("成功连接到Neo4j数据库。")
except Exception as e:
    print(f"连接Neo4j失败: {e}")
    exit()

# 确认文件路径
file_path = 'F:\\ddg\\KG\\图谱\\结泥饼纯三元组.xlsx'
#file_path = 'F:\\ddg\\KG\\图谱\\滞排纯三元组.xlsx'
#file_path = 'F:\\ddg\\KG\\图谱\\盾尾密封失效纯三元组.xlsx'
#file_path = 'F:\\ddg\\KG\\图谱\\主轴承损坏纯三元组.xlsx'

if not os.path.exists(file_path):
    print(f"文件不存在: {file_path}")
    exit()

# 读取Excel文件
try:
    df = pd.read_excel(file_path, header=None, names=["A", "relation", "B"], skiprows=1)
    print(f"成功读取数据，共 {len(df)} 条三元组")
except Exception as e:
    print(f"读取Excel失败: {e}")
    exit()
# 在 df = pd.read_excel(...) 之后添加
df["relation"] = df["relation"].astype(str).str.strip()  # 强制转换为字符串并去空格

# 批量处理节点和关系
batch_size = 1000  # 每批处理数量
tx = graph.begin()
nodes = {}  # 节点缓存字典

for index, row in df.iterrows():
    try:
        # 处理头节点
        head_name = str(row["A"]).strip()
        if head_name not in nodes:
            head_node = Node("Entity", name=head_name)
            nodes[head_name] = head_node
            tx.create(head_node)

        # 处理尾节点
        tail_name = str(row["B"]).strip()
        if tail_name not in nodes:
            tail_node = Node("Entity", name=tail_name)
            nodes[tail_name] = tail_node
            tx.create(tail_node)

        # 创建关系
        rel = Relationship(nodes[head_name], str(row["relation"]).strip(), nodes[tail_name])
        tx.create(rel)

        # 批量提交
        if index % batch_size == 0 and index != 0:
            graph.commit(tx)
            tx = graph.begin()
            print(f"已提交 {index} 条数据")

    except Exception as e:
        print(f"处理第 {index} 行时出错: {e}")
        continue

# 提交剩余数据
try:
    graph.commit(tx)
    print("数据导入完成，共处理 {} 个节点，{} 条关系".format(len(nodes), len(df)))
except Exception as e:
    print(f"最终提交失败: {e}")

# 创建索引加速查询
try:
    graph.run("CREATE INDEX entity_name IF NOT EXISTS FOR (n:Entity) ON (n.name)")
    print("已创建节点名称索引")
except Exception as e:
    print(f"创建索引失败: {e}")
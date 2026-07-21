import pandas as pd
from py2neo import Graph, Node, Relationship, Subgraph
import os

# 连接到Neo4j数据库
try:
    graph = Graph('bolt://localhost:7687', auth=("neo4j", "xty328310"))
    
    # 完全清理数据库 - 删除所有数据、索引和约束
    print("正在清理Neo4j数据库...")
    graph.run("MATCH (n) DETACH DELETE n")  # 删除所有节点和关系
    graph.run("DROP INDEX entity_name IF EXISTS")  # 删除实体名称索引
    
    # 可选：删除其他可能存在的索引和约束
    try:
        # 获取并删除所有索引
        indexes = graph.run("SHOW INDEXES").data()
        for index in indexes:
            if 'name' in index:
                graph.run(f"DROP INDEX {index['name']} IF EXISTS")
        
        # 获取并删除所有约束
        constraints = graph.run("SHOW CONSTRAINTS").data()
        for constraint in constraints:
            if 'name' in constraint:
                graph.run(f"DROP CONSTRAINT {constraint['name']} IF EXISTS")
                
    except Exception as e:
        print(f"清理索引/约束时出错（可忽略）: {e}")
    
    print("数据库清理完成")
    
    # 验证清理结果
    try:
        node_count = graph.run("MATCH (n) RETURN count(n) as count").data()[0]['count']
        rel_count = graph.run("MATCH ()-[r]->() RETURN count(r) as count").data()[0]['count']
        index_count = len(graph.run("SHOW INDEXES").data())
        constraint_count = len(graph.run("SHOW CONSTRAINTS").data())
        
        print(f"验证清理结果:")
        print(f"  - 剩余节点数: {node_count}")
        print(f"  - 剩余关系数: {rel_count}")
        print(f"  - 剩余索引数: {index_count}")
        print(f"  - 剩余约束数: {constraint_count}")
        
        if node_count == 0 and rel_count == 0:
            print("✅ 数据清理成功")
        else:
            print("⚠️  警告: 仍有数据残留")
            
    except Exception as e:
        print(f"验证清理结果时出错: {e}")
    
    print("成功连接到Neo4j数据库。")
except Exception as e:
    print(f"连接Neo4j失败: {e}")
    exit()

# 确认文件路径
#file_path = 'F:\\ddg\\KG\\图谱\\结泥饼纯三元组.xlsx'
#file_path = 'F:\\ddg\\KG\\图谱\\滞排纯三元组.xlsx'
#file_path = 'F:\\ddg\\KG\\图谱\\盾尾密封失效纯三元组.xlsx'
#file_path = 'F:\\ddg\\KG\\图谱\\主轴承损坏纯三元组.xlsx'
file_path = 'F:\ddg\KG\带压进仓_纯三元组.xlsx'

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
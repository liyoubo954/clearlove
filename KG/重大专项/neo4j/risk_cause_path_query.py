import json
from py2neo import Graph, NodeMatcher

def connect_to_neo4j():
    """连接到Neo4j数据库"""
    try:
        graph = Graph('bolt://localhost:7687', auth=("neo4j", "xty328310"))
        print("成功连接到Neo4j数据库。")
        return graph
    except Exception as e:
        print(f"连接Neo4j失败: {e}")
        return None

def find_paths_from_cause(graph, cause_name):
    """
    从指定的风险原因节点开始，查找到所有后续节点的路径
    返回符合records.json格式的结果
    """
    # Cypher查询：从指定原因节点开始，找到所有可达的路径
    cypher_query = """
    MATCH path = (start {name: $cause_name})-[*1..10]->(end)
    WHERE NOT (end)-->()  // 只返回到终端节点的路径
    RETURN path, 
           nodes(path) as path_nodes, 
           relationships(path) as path_relationships,
           length(path) as path_length
    ORDER BY path_length, end.name
    """
    
    try:
        result = graph.run(cypher_query, cause_name=cause_name)
        paths_data = []
        
        for record in result:
            path_nodes = record["path_nodes"]
            path_relationships = record["path_relationships"]
            path_length = record["path_length"]
            
            # 构建路径数据，格式类似records.json
            path_info = {
                "path_length": path_length,
                "nodes": [],
                "relationships": []
            }
            
            # 添加路径中的所有节点
            for node in path_nodes:
                node_data = {
                    "identity": node.identity,
                    "labels": list(node.labels),
                    "properties": dict(node),
                    "elementId": str(node.element_id) if hasattr(node, 'element_id') else f"node_{node.identity}"
                }
                path_info["nodes"].append({"n": node_data})
            
            # 添加路径中的所有关系
            for rel in path_relationships:
                rel_data = {
                    "identity": rel.identity,
                    "type": type(rel).__name__,
                    "properties": dict(rel),
                    "start_node_id": rel.start_node.identity,
                    "end_node_id": rel.end_node.identity,
                    "elementId": str(rel.element_id) if hasattr(rel, 'element_id') else f"rel_{rel.identity}"
                }
                path_info["relationships"].append({"r": rel_data})
            
            paths_data.append(path_info)
        
        return paths_data
        
    except Exception as e:
        print(f"查询路径时出错: {e}")
        return []

def find_complete_paths_from_cause(graph, cause_name):
    """
    从指定的风险原因节点开始，查找完整的路径（从风险名称开始到该原因，再到所有后续节点）
    返回格式类似records.json的节点列表
    """
    # 首先找到包含该原因的风险名称
    risk_query = """
    MATCH (risk:风险名称)-[*1..3]->(cause {name: $cause_name})
    RETURN risk
    LIMIT 1
    """
    
    risk_result = graph.run(risk_query, cause_name=cause_name)
    risk_node = None
    
    for record in risk_result:
        risk_node = record["risk"]
        break
    
    if not risk_node:
        print(f"未找到包含原因 '{cause_name}' 的风险名称")
        return []
    
    # 查找从风险名称到原因，再到所有后续节点的完整路径
    complete_query = """
    MATCH path = (risk:风险名称 {name: $risk_name})-[*1..15]->(end)
    WHERE ANY(node IN nodes(path) WHERE node.name = $cause_name)
    AND NOT (end)-->()  // 只返回到终端节点的路径
    WITH path, nodes(path) as path_nodes, relationships(path) as path_relationships
    WHERE ANY(i IN range(0, size(path_nodes)-1) WHERE path_nodes[i].name = $cause_name)
    RETURN DISTINCT path_nodes, path_relationships, length(path) as path_length
    ORDER BY path_length
    """
    
    try:
        result = graph.run(complete_query, risk_name=risk_node["name"], cause_name=cause_name)
        all_nodes = []
        processed_nodes = set()
        
        for record in result:
            path_nodes = record["path_nodes"]
            
            # 添加路径中的所有节点（避免重复）
            for node in path_nodes:
                node_id = node.identity
                if node_id not in processed_nodes:
                    processed_nodes.add(node_id)
                    
                    node_data = {
                        "identity": node.identity,
                        "labels": list(node.labels),
                        "properties": dict(node),
                        "elementId": str(node.element_id) if hasattr(node, 'element_id') else f"4:20c054e7-3aea-464a-8411-52b71cd5c7b9:{node.identity}"
                    }
                    all_nodes.append({"n": node_data})
        
        return all_nodes
        
    except Exception as e:
        print(f"查询完整路径时出错: {e}")
        return []

def get_complete_path_from_cause(graph, cause_name):
    """
    获取从风险名称开始，经过指定原因，到所有后续节点的完整路径
    返回格式完全模仿records.json，包含风险名称节点
    """
    # 查找包含该原因的完整路径上的所有节点，包括风险名称
    query = """
    MATCH (risk:风险名称)-[*1..3]->(cause {name: $cause_name})
    WITH risk, cause
    MATCH path = (risk)-[*0..10]->(node)
    WHERE ANY(n IN nodes(path) WHERE n.name = $cause_name)
    RETURN DISTINCT node
    UNION
    MATCH (risk:风险名称)-[*1..3]->(cause {name: $cause_name})
    RETURN DISTINCT risk as node
    ORDER BY 
        CASE 
            WHEN '风险名称' IN labels(node) THEN 1
            WHEN node.name = $cause_name THEN 2
            WHEN '措施' IN labels(node) THEN 3
            ELSE 4
        END,
        node.name
    """
    
    try:
        result = graph.run(query, cause_name=cause_name)
        nodes_list = []
        
        for record in result:
            node = record["node"]
            node_data = {
                "identity": node.identity,
                "labels": list(node.labels),
                "properties": dict(node),
                "elementId": f"4:20c054e7-3aea-464a-8411-52b71cd5c7b9:{node.identity}"
            }
            nodes_list.append({"n": node_data})
        
        return nodes_list
        
    except Exception as e:
        print(f"查询节点时出错: {e}")
        return []

def main():
    # 连接数据库
    graph = connect_to_neo4j()
    if not graph:
        return
    
    # 指定要查询的风险原因
    cause_name = "泡沫注入量不足"
    
    print(f"正在查询从原因 '{cause_name}' 开始的所有相关节点...")
    
    # 查找所有相关节点，格式类似records.json
    all_nodes = get_complete_path_from_cause(graph, cause_name)
    
    if all_nodes:
        # 保存结果到JSON文件
        output_file = f"risk_cause_nodes_{cause_name.replace('/', '_')}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_nodes, f, ensure_ascii=False, indent=2)
        
        print(f"查询完成，找到 {len(all_nodes)} 个相关节点")
        print(f"结果已保存到: {output_file}")
        
        # 打印节点类型统计
        label_counts = {}
        for node_item in all_nodes:
            node = node_item["n"]
            for label in node["labels"]:
                if label != "Entity":  # 排除通用Entity标签
                    label_counts[label] = label_counts.get(label, 0) + 1
        
        print("\n节点类型统计:")
        for label, count in sorted(label_counts.items()):
            print(f"  {label}: {count} 个")
        
        # 打印部分节点示例
        print(f"\n前5个节点示例:")
        for i, node_item in enumerate(all_nodes[:5]):
            node = node_item["n"]
            main_label = [l for l in node["labels"] if l != "Entity"][0] if len([l for l in node["labels"] if l != "Entity"]) > 0 else "Entity"
            print(f"  {i+1}. [{main_label}] {node['properties'].get('name', 'N/A')}")
    else:
        print("未找到任何相关节点")

if __name__ == "__main__":
    main()
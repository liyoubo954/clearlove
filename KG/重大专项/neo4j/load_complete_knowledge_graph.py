#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整的Neo4j知识图谱数据导入脚本
整合三元组数据和实体属性数据的导入功能
"""

import pandas as pd
from py2neo import Graph, Node, Relationship, NodeMatcher
import os
import logging
from typing import Dict, Set, Tuple

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Neo4jKnowledgeGraphLoader:
    def __init__(self, uri: str = 'bolt://localhost:7687', username: str = "neo4j", password: str = "xty328310"):
        """
        初始化Neo4j知识图谱加载器
        
        Args:
            uri: Neo4j数据库连接URI
            username: 用户名
            password: 密码
        """
        self.graph = None
        self.nodes_cache = {}  # 节点缓存
        self.batch_size = 1000  # 批处理大小
        
        try:
            self.graph = Graph(uri, auth=(username, password))
            logger.info("成功连接到Neo4j数据库")
        except Exception as e:
            logger.error(f"连接Neo4j数据库失败: {e}")
            raise
    
    def clear_database(self):
        """清空数据库"""
        try:
            self.graph.delete_all()
            logger.info("已清空数据库")
        except Exception as e:
            logger.error(f"清空数据库失败: {e}")
            raise
    
    def load_triplets(self, file_path: str):
        """
        加载三元组数据
        
        Args:
            file_path: 三元组Excel文件路径
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"三元组文件不存在: {file_path}")
        
        try:
            # 读取三元组数据
            df = pd.read_excel(file_path)
            logger.info(f"成功读取三元组数据，共 {len(df)} 条记录")
            
            # 数据清洗
            df = df.dropna()  # 删除空值行
            df['首实体'] = df['首实体'].astype(str).str.strip()
            df['关系'] = df['关系'].astype(str).str.strip()
            df['尾实体'] = df['尾实体'].astype(str).str.strip()
            
            # 批量处理
            tx = self.graph.begin()
            processed_count = 0
            
            for index, row in df.iterrows():
                try:
                    head_entity = row['首实体']
                    relation = row['关系']
                    tail_entity = row['尾实体']
                    
                    # 创建或获取头实体节点
                    if head_entity not in self.nodes_cache:
                        head_node = Node("Entity", name=head_entity)
                        self.nodes_cache[head_entity] = head_node
                        tx.create(head_node)
                    
                    # 创建或获取尾实体节点
                    if tail_entity not in self.nodes_cache:
                        tail_node = Node("Entity", name=tail_entity)
                        self.nodes_cache[tail_entity] = tail_node
                        tx.create(tail_node)
                    
                    # 创建关系
                    rel = Relationship(
                        self.nodes_cache[head_entity], 
                        relation, 
                        self.nodes_cache[tail_entity]
                    )
                    tx.create(rel)
                    
                    processed_count += 1
                    
                    # 批量提交
                    if processed_count % self.batch_size == 0:
                        self.graph.commit(tx)
                        tx = self.graph.begin()
                        logger.info(f"已处理 {processed_count} 条三元组")
                        
                except Exception as e:
                    logger.error(f"处理第 {index} 行三元组时出错: {e}")
                    continue
            
            # 提交剩余数据
            self.graph.commit(tx)
            logger.info(f"三元组数据导入完成，共处理 {processed_count} 条记录")
            
        except Exception as e:
            logger.error(f"加载三元组数据失败: {e}")
            raise
    
    def load_entity_attributes(self, file_path: str):
        """
        加载实体属性数据
        
        Args:
            file_path: 实体属性Excel文件路径
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"实体属性文件不存在: {file_path}")
        
        try:
            # 读取实体属性数据
            df = pd.read_excel(file_path)
            logger.info(f"成功读取实体属性数据，共 {len(df)} 条记录")
            
            # 数据清洗
            df = df.dropna()
            df['实体名称'] = df['实体名称'].astype(str).str.strip()
            df['实体类型'] = df['实体类型'].astype(str).str.strip()
            df['属性'] = df['属性'].astype(str).str.strip()
            df['属性描述'] = df['属性描述'].astype(str).str.strip()
            
            # 使用NodeMatcher来更新现有节点
            matcher = NodeMatcher(self.graph)
            processed_count = 0
            
            for index, row in df.iterrows():
                try:
                    entity_name = row['实体名称']
                    entity_type = row['实体类型']
                    attribute_name = row['属性']
                    attribute_value = row['属性描述']
                    
                    # 查找现有节点
                    node = matcher.match("Entity", name=entity_name).first()
                    
                    if node:
                        # 更新节点标签（添加实体类型作为标签）
                        if entity_type and entity_type != 'Entity':
                            # 清除旧标签并添加新标签
                            node.clear_labels()
                            node.add_label("Entity")  # 保留基础Entity标签
                            node.add_label(entity_type)  # 添加具体类型标签
                        
                        # 添加属性
                        if attribute_name and attribute_value:
                            node[attribute_name] = attribute_value
                        
                        # 提交更新
                        self.graph.push(node)
                        processed_count += 1
                        
                        if processed_count % 100 == 0:
                            logger.info(f"已更新 {processed_count} 个实体属性")
                    else:
                        # 如果节点不存在，创建新节点
                        labels = ["Entity"]
                        if entity_type and entity_type != 'Entity':
                            labels.append(entity_type)
                        
                        new_node = Node(*labels, name=entity_name)
                        if attribute_name and attribute_value:
                            new_node[attribute_name] = attribute_value
                        
                        self.graph.create(new_node)
                        self.nodes_cache[entity_name] = new_node
                        processed_count += 1
                        
                        logger.info(f"创建新节点: {entity_name}")
                        
                except Exception as e:
                    logger.error(f"处理第 {index} 行实体属性时出错: {e}")
                    continue
            
            logger.info(f"实体属性数据导入完成，共处理 {processed_count} 条记录")
            
        except Exception as e:
            logger.error(f"加载实体属性数据失败: {e}")
            raise
    
    def create_indexes(self):
        """创建索引以提高查询性能"""
        try:
            # 为Entity节点的name属性创建索引
            self.graph.run("CREATE INDEX entity_name_idx IF NOT EXISTS FOR (n:Entity) ON (n.name)")
            
            # 为不同类型的节点创建索引
            entity_types = ["风险名称", "地质原因", "设备原因", "操作原因", "环境原因"]
            for entity_type in entity_types:
                try:
                    self.graph.run(f"CREATE INDEX {entity_type.replace(' ', '_')}_name_idx IF NOT EXISTS FOR (n:`{entity_type}`) ON (n.name)")
                except:
                    pass  # 如果标签不存在，忽略错误
            
            logger.info("索引创建完成")
            
        except Exception as e:
            logger.error(f"创建索引失败: {e}")
    
    def get_statistics(self):
        """获取数据库统计信息"""
        try:
            # 节点统计
            node_count = self.graph.run("MATCH (n) RETURN count(n) as count").data()[0]['count']
            
            # 关系统计
            rel_count = self.graph.run("MATCH ()-[r]->() RETURN count(r) as count").data()[0]['count']
            
            # 标签统计
            labels_result = self.graph.run("CALL db.labels()").data()
            labels = [item['label'] for item in labels_result]
            
            # 关系类型统计
            rel_types_result = self.graph.run("CALL db.relationshipTypes()").data()
            rel_types = [item['relationshipType'] for item in rel_types_result]
            
            logger.info(f"数据库统计信息:")
            logger.info(f"  节点数量: {node_count}")
            logger.info(f"  关系数量: {rel_count}")
            logger.info(f"  节点标签: {labels}")
            logger.info(f"  关系类型: {rel_types}")
            
            return {
                'nodes': node_count,
                'relationships': rel_count,
                'labels': labels,
                'relationship_types': rel_types
            }
            
        except Exception as e:
            logger.error(f"获取统计信息失败: {e}")
            return None

def main():
    """主函数"""
    # 文件路径配置
    triplets_file = 'F:\\ddg\\KG\\重大专项\\最终_纯三元组.xlsx'
    attributes_file = 'F:\\ddg\\KG\\重大专项\\最终_类型描述.xlsx'
    
    try:
        # 初始化加载器
        loader = Neo4jKnowledgeGraphLoader()
        
        # 清空数据库（可选）
        user_input = input("是否清空现有数据库？(y/N): ").strip().lower()
        if user_input == 'y':
            loader.clear_database()
        
        # 加载三元组数据
        logger.info("开始加载三元组数据...")
        loader.load_triplets(triplets_file)
        
        # 加载实体属性数据
        logger.info("开始加载实体属性数据...")
        loader.load_entity_attributes(attributes_file)
        
        # 创建索引
        logger.info("创建索引...")
        loader.create_indexes()
        
        # 显示统计信息
        logger.info("获取数据库统计信息...")
        stats = loader.get_statistics()
        
        logger.info("知识图谱数据导入完成！")
        
    except Exception as e:
        logger.error(f"数据导入过程中发生错误: {e}")
        raise

if __name__ == "__main__":
    main()
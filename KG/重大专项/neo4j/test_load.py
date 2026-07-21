#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试Neo4j知识图谱数据导入功能
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from load_complete_knowledge_graph import Neo4jKnowledgeGraphLoader
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_connection():
    """测试数据库连接"""
    try:
        loader = Neo4jKnowledgeGraphLoader()
        logger.info("✓ 数据库连接测试成功")
        return loader
    except Exception as e:
        logger.error(f"✗ 数据库连接测试失败: {e}")
        return None

def test_data_loading(loader):
    """测试数据加载功能"""
    triplets_file = 'F:\\ddg\\KG\\重大专项\\最终_纯三元组.xlsx'
    attributes_file = 'F:\\ddg\\KG\\重大专项\\最终_类型描述.xlsx'
    
    try:
        # 测试文件是否存在
        if not os.path.exists(triplets_file):
            logger.error(f"✗ 三元组文件不存在: {triplets_file}")
            return False
        
        if not os.path.exists(attributes_file):
            logger.error(f"✗ 属性文件不存在: {attributes_file}")
            return False
        
        logger.info("✓ 数据文件存在检查通过")
        
        # 清空数据库进行测试
        loader.clear_database()
        logger.info("✓ 数据库清空成功")
        
        # 加载三元组数据
        loader.load_triplets(triplets_file)
        logger.info("✓ 三元组数据加载成功")
        
        # 加载实体属性数据
        loader.load_entity_attributes(attributes_file)
        logger.info("✓ 实体属性数据加载成功")
        
        # 创建索引
        loader.create_indexes()
        logger.info("✓ 索引创建成功")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ 数据加载测试失败: {e}")
        return False

def test_data_verification(loader):
    """验证导入的数据"""
    try:
        # 获取统计信息
        stats = loader.get_statistics()
        
        if stats:
            logger.info("✓ 数据验证成功")
            logger.info(f"  - 节点数量: {stats['nodes']}")
            logger.info(f"  - 关系数量: {stats['relationships']}")
            logger.info(f"  - 节点标签: {stats['labels']}")
            logger.info(f"  - 关系类型: {stats['relationship_types']}")
            
            # 基本验证
            if stats['nodes'] > 0 and stats['relationships'] > 0:
                logger.info("✓ 数据导入验证通过")
                return True
            else:
                logger.error("✗ 数据导入验证失败：节点或关系数量为0")
                return False
        else:
            logger.error("✗ 无法获取统计信息")
            return False
            
    except Exception as e:
        logger.error(f"✗ 数据验证失败: {e}")
        return False

def test_sample_queries(loader):
    """测试示例查询"""
    try:
        # 查询示例1：获取所有风险名称节点
        result1 = loader.graph.run("MATCH (n:风险名称) RETURN n.name LIMIT 5").data()
        logger.info(f"✓ 风险名称节点查询成功，找到 {len(result1)} 个节点")
        
        # 查询示例2：获取所有关系类型
        result2 = loader.graph.run("MATCH ()-[r]->() RETURN DISTINCT type(r) LIMIT 10").data()
        logger.info(f"✓ 关系类型查询成功，找到 {len(result2)} 种关系类型")
        
        # 查询示例3：获取具有描述属性的节点
        result3 = loader.graph.run("MATCH (n) WHERE n.描述 IS NOT NULL RETURN n.name, n.描述 LIMIT 3").data()
        logger.info(f"✓ 属性查询成功，找到 {len(result3)} 个有描述的节点")
        
        if result3:
            for item in result3:
                logger.info(f"  - {item['n.name']}: {item['n.描述'][:50]}...")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ 示例查询测试失败: {e}")
        return False

def main():
    """主测试函数"""
    logger.info("开始Neo4j知识图谱数据导入测试...")
    
    # 测试连接
    loader = test_connection()
    if not loader:
        return
    
    # 测试数据加载
    if not test_data_loading(loader):
        return
    
    # 验证数据
    if not test_data_verification(loader):
        return
    
    # 测试查询
    if not test_sample_queries(loader):
        return
    
    logger.info("🎉 所有测试通过！知识图谱数据导入功能正常")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱信息提取脚本
从JSON文件中提取：
1. 首实体-关系-尾实体三元组表
2. 实体-实体类型-属性-属性值表
"""

import json
import pandas as pd
from collections import defaultdict
import os

def load_json_data(file_path):
    """加载JSON数据"""
    try:
        # 尝试使用utf-8-sig编码处理BOM
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
        print(f"成功加载JSON文件，包含 {len(data)} 条记录")
        return data
    except Exception as e:
        # 如果utf-8-sig失败，尝试普通utf-8
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"成功加载JSON文件，包含 {len(data)} 条记录")
            return data
        except Exception as e2:
            print(f"加载JSON文件时出错: {e2}")
            return None

def extract_triples(data):
    """提取首实体-关系-尾实体三元组"""
    triples = []
    
    for item in data:
        if 'p' in item and 'segments' in item['p']:
            for segment in item['p']['segments']:
                # 提取起始实体信息
                start_node = segment['start']
                start_entity = start_node['properties'].get('name', '')
                start_labels = ', '.join(start_node.get('labels', []))
                
                # 提取关系信息
                relationship = segment['relationship']
                relation_type = relationship.get('type', '')
                
                # 提取结束实体信息
                end_node = segment['end']
                end_entity = end_node['properties'].get('name', '')
                end_labels = ', '.join(end_node.get('labels', []))
                
                # 添加三元组
                triple = {
                    '首实体': start_entity,
                    '首实体类型': start_labels,
                    '关系': relation_type,
                    '尾实体': end_entity,
                    '尾实体类型': end_labels,
                    '关系ID': relationship.get('identity', ''),
                    '首实体ID': start_node.get('identity', ''),
                    '尾实体ID': end_node.get('identity', '')
                }
                triples.append(triple)
    
    return triples

def extract_entity_attributes(data):
    """提取实体-实体类型-属性-属性值信息"""
    entities = {}
    
    for item in data:
        if 'p' in item:
            # 处理起始节点和结束节点
            nodes = []
            if 'start' in item['p']:
                nodes.append(item['p']['start'])
            if 'end' in item['p']:
                nodes.append(item['p']['end'])
            
            # 处理segments中的节点
            if 'segments' in item['p']:
                for segment in item['p']['segments']:
                    if 'start' in segment:
                        nodes.append(segment['start'])
                    if 'end' in segment:
                        nodes.append(segment['end'])
            
            # 提取每个节点的属性
            for node in nodes:
                entity_id = node.get('identity', '')
                entity_name = node['properties'].get('name', '')
                entity_labels = ', '.join(node.get('labels', []))
                
                # 使用实体ID作为唯一标识符
                if entity_id not in entities:
                    entities[entity_id] = {
                        '实体名称': entity_name,
                        '实体类型': entity_labels,
                        '实体ID': entity_id,
                        '属性': {}
                    }
                
                # 提取所有属性
                properties = node.get('properties', {})
                for prop_key, prop_value in properties.items():
                    if prop_key != 'name':  # name已经作为实体名称处理
                        entities[entity_id]['属性'][prop_key] = prop_value
    
    # 转换为表格格式
    entity_attributes = []
    for entity_id, entity_info in entities.items():
        if entity_info['属性']:
            # 如果有属性，为每个属性创建一行
            for attr_name, attr_value in entity_info['属性'].items():
                entity_attributes.append({
                    '实体名称': entity_info['实体名称'],
                    '实体类型': entity_info['实体类型'],
                    '实体ID': entity_info['实体ID'],
                    '属性名称': attr_name,
                    '属性值': attr_value
                })
        else:
            # 如果没有属性，创建一行空属性记录
            entity_attributes.append({
                '实体名称': entity_info['实体名称'],
                '实体类型': entity_info['实体类型'],
                '实体ID': entity_info['实体ID'],
                '属性名称': '',
                '属性值': ''
            })
    
    return entity_attributes

def analyze_data_completeness(data, triples, entity_attributes):
    """分析数据完整性，检查是否有信息遗漏"""
    analysis = {
        '总记录数': len(data),
        '三元组数量': len(triples),
        '唯一实体数量': len(set([t['首实体'] for t in triples] + [t['尾实体'] for t in triples])),
        '唯一关系类型': list(set([t['关系'] for t in triples])),
        '实体类型统计': {},
        '属性统计': {},
        '可能遗漏的信息': []
    }
    
    # 统计实体类型
    entity_types = defaultdict(int)
    for attr in entity_attributes:
        if attr['实体类型']:
            entity_types[attr['实体类型']] += 1
    analysis['实体类型统计'] = dict(entity_types)
    
    # 统计属性类型
    attr_types = defaultdict(int)
    for attr in entity_attributes:
        if attr['属性名称']:
            attr_types[attr['属性名称']] += 1
    analysis['属性统计'] = dict(attr_types)
    
    # 检查可能遗漏的信息
    sample_item = data[0] if data else {}
    if 'p' in sample_item:
        if 'length' in sample_item['p']:
            analysis['可能遗漏的信息'].append('路径长度信息 (length)')
        
        # 检查关系属性
        has_relation_props = False
        if 'segments' in sample_item['p']:
            for segment in sample_item['p']['segments']:
                if 'relationship' in segment and segment['relationship'].get('properties'):
                    has_relation_props = True
                    break
        
        if not has_relation_props:
            analysis['可能遗漏的信息'].append('关系可能包含额外属性信息')
    
    return analysis

def save_to_excel(triples, entity_attributes, analysis, output_file):
    """保存结果到Excel文件"""
    try:
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # 保存三元组表
            triples_df = pd.DataFrame(triples)
            triples_df.to_excel(writer, sheet_name='三元组表', index=False)
            
            # 保存实体属性表
            entity_df = pd.DataFrame(entity_attributes)
            entity_df.to_excel(writer, sheet_name='实体属性表', index=False)
            
            # 保存分析报告
            analysis_data = []
            for key, value in analysis.items():
                if isinstance(value, (dict, list)):
                    analysis_data.append({'项目': key, '值': str(value)})
                else:
                    analysis_data.append({'项目': key, '值': value})
            
            analysis_df = pd.DataFrame(analysis_data)
            analysis_df.to_excel(writer, sheet_name='数据分析报告', index=False)
        
        print(f"结果已保存到: {output_file}")
        return True
    except Exception as e:
        print(f"保存Excel文件时出错: {e}")
        return False

def save_to_csv(triples, entity_attributes, output_dir):
    """保存结果到CSV文件"""
    try:
        # 保存三元组表
        triples_df = pd.DataFrame(triples)
        triples_file = os.path.join(output_dir, '三元组表.csv')
        triples_df.to_csv(triples_file, index=False, encoding='utf-8-sig')
        
        # 保存实体属性表
        entity_df = pd.DataFrame(entity_attributes)
        entity_file = os.path.join(output_dir, '实体属性表.csv')
        entity_df.to_csv(entity_file, index=False, encoding='utf-8-sig')
        
        print(f"CSV文件已保存到: {output_dir}")
        return True
    except Exception as e:
        print(f"保存CSV文件时出错: {e}")
        return False

def main():
    """主函数"""
    # 输入文件路径
    input_file = "结泥饼.json"
    
    # 检查文件是否存在
    if not os.path.exists(input_file):
        print(f"错误: 找不到文件 {input_file}")
        return
    
    print("开始处理知识图谱数据...")
    
    # 加载数据
    data = load_json_data(input_file)
    if not data:
        return
    
    # 提取三元组
    print("提取三元组信息...")
    triples = extract_triples(data)
    print(f"提取到 {len(triples)} 个三元组")
    
    # 提取实体属性
    print("提取实体属性信息...")
    entity_attributes = extract_entity_attributes(data)
    print(f"提取到 {len(entity_attributes)} 条实体属性记录")
    
    # 分析数据完整性
    print("分析数据完整性...")
    analysis = analyze_data_completeness(data, triples, entity_attributes)
    
    # 打印分析结果
    print("\n=== 数据分析报告 ===")
    print(f"总记录数: {analysis['总记录数']}")
    print(f"三元组数量: {analysis['三元组数量']}")
    print(f"唯一实体数量: {analysis['唯一实体数量']}")
    print(f"关系类型: {analysis['唯一关系类型']}")
    print(f"实体类型统计: {analysis['实体类型统计']}")
    print(f"属性统计: {analysis['属性统计']}")
    if analysis['可能遗漏的信息']:
        print(f"可能遗漏的信息: {analysis['可能遗漏的信息']}")
    
    # 保存结果
    print("\n保存结果...")
    
    # 保存为Excel文件
    excel_file = "知识图谱提取结果.xlsx"
    save_to_excel(triples, entity_attributes, analysis, excel_file)
    
    # 保存为CSV文件
    save_to_csv(triples, entity_attributes, ".")
    
    print("\n处理完成!")
    
    # 显示前几条记录作为示例
    print("\n=== 三元组示例 (前5条) ===")
    for i, triple in enumerate(triples[:5]):
        print(f"{i+1}. {triple['首实体']} --[{triple['关系']}]--> {triple['尾实体']}")
    
    print("\n=== 实体属性示例 (前5条) ===")
    for i, attr in enumerate(entity_attributes[:5]):
        if attr['属性名称']:
            print(f"{i+1}. {attr['实体名称']} ({attr['实体类型']}) - {attr['属性名称']}: {attr['属性值']}")
        else:
            print(f"{i+1}. {attr['实体名称']} ({attr['实体类型']}) - 无额外属性")

if __name__ == "__main__":
    main()
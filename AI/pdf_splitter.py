#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF文件分割工具
根据big_output目录中的文件模式，这个工具可以将大PDF文件分割成多个小文件
"""

import os
import sys
from pathlib import Path
try:
    import PyPDF2
except ImportError:
    print("请先安装PyPDF2: pip install PyPDF2")
    sys.exit(1)

def split_pdf(input_path, output_dir, pages_per_file=50):
    """
    将PDF文件分割成多个小文件
    
    Args:
        input_path (str): 输入PDF文件路径
        output_dir (str): 输出目录
        pages_per_file (int): 每个文件包含的页数，默认50页
    """
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    
    if not input_path.exists():
        print(f"错误：输入文件不存在 {input_path}")
        return False
    
    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(input_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)
            
            print(f"正在处理文件: {input_path.name}")
            print(f"总页数: {total_pages}")
            print(f"每个文件页数: {pages_per_file}")
            
            # 计算需要分割的文件数量
            num_files = (total_pages + pages_per_file - 1) // pages_per_file
            print(f"将分割为 {num_files} 个文件")
            
            base_name = input_path.stem  # 不包含扩展名的文件名
            
            for i in range(num_files):
                start_page = i * pages_per_file
                end_page = min((i + 1) * pages_per_file, total_pages)
                
                # 创建新的PDF写入器
                pdf_writer = PyPDF2.PdfWriter()
                
                # 添加页面到新PDF
                for page_num in range(start_page, end_page):
                    pdf_writer.add_page(pdf_reader.pages[page_num])
                
                # 生成输出文件名
                output_filename = f"{base_name}_part{i+1}.pdf"
                output_path = output_dir / output_filename
                
                # 写入文件
                with open(output_path, 'wb') as output_file:
                    pdf_writer.write(output_file)
                
                print(f"已创建: {output_filename} (页面 {start_page+1}-{end_page})")
            
            print(f"\n分割完成！输出目录: {output_dir}")
            return True
            
    except Exception as e:
        print(f"错误：处理PDF文件时出现问题 - {str(e)}")
        return False

def main():
    """
    主函数 - 处理命令行参数
    """
    if len(sys.argv) < 2:
        print("使用方法:")
        print(f"  python {sys.argv[0]} <PDF文件路径> [输出目录] [每个文件页数]")
        print("\n示例:")
        print(f"  python {sys.argv[0]} big/【CRCC】盾构机操作手培训教材.pdf big_output 50")
        print(f"  python {sys.argv[0]} big/盾构施工标准化手册.pdf big_output/附件：2 30")
        return
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"
    pages_per_file = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    
    print(f"输入文件: {input_file}")
    print(f"输出目录: {output_dir}")
    print(f"每个文件页数: {pages_per_file}")
    print("-" * 50)
    
    success = split_pdf(input_file, output_dir, pages_per_file)
    
    if success:
        print("\n✅ PDF分割成功完成！")
    else:
        print("\n❌ PDF分割失败！")
        sys.exit(1)

if __name__ == "__main__":
    main()
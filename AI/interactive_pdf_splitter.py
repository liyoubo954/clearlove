#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交互式PDF分割工具
允许用户选择PDF文件并设置分割参数
"""

import os
import sys
from pathlib import Path
import glob

try:
    import PyPDF2
except ImportError:
    print("正在安装PyPDF2...")
    os.system("pip install PyPDF2")
    try:
        import PyPDF2
    except ImportError:
        print("错误：无法安装PyPDF2，请手动安装: pip install PyPDF2")
        sys.exit(1)

def find_pdf_files(directory="."):
    """
    在指定目录及其子目录中查找PDF文件
    """
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def get_pdf_info(pdf_path):
    """
    获取PDF文件信息
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            pages = len(pdf_reader.pages)
            size = os.path.getsize(pdf_path) / (1024 * 1024)  # MB
            return pages, size
    except:
        return None, None

def split_pdf(input_path, output_dir, pages_per_file=50):
    """
    分割PDF文件
    """
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    
    if not input_path.exists():
        print(f"❌ 错误：输入文件不存在 {input_path}")
        return False
    
    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(input_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)
            
            print(f"\n📄 正在处理: {input_path.name}")
            print(f"📊 总页数: {total_pages}")
            print(f"📑 每个文件页数: {pages_per_file}")
            
            # 计算需要分割的文件数量
            num_files = (total_pages + pages_per_file - 1) // pages_per_file
            print(f"📁 将分割为 {num_files} 个文件")
            print("-" * 50)
            
            base_name = input_path.stem
            
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
                
                print(f"✅ 已创建: {output_filename} (页面 {start_page+1}-{end_page})")
            
            print(f"\n🎉 分割完成！输出目录: {output_dir}")
            return True
            
    except Exception as e:
        print(f"❌ 错误：处理PDF文件时出现问题 - {str(e)}")
        return False

def main():
    """
    主交互函数
    """
    print("="*60)
    print("           📚 交互式PDF分割工具 📚")
    print("="*60)
    
    # 查找PDF文件
    print("\n🔍 正在搜索PDF文件...")
    pdf_files = find_pdf_files()
    
    if not pdf_files:
        print("❌ 未找到任何PDF文件")
        input("按回车键退出...")
        return
    
    print(f"\n📋 找到 {len(pdf_files)} 个PDF文件：")
    print("-" * 60)
    
    # 显示PDF文件列表
    for i, pdf_file in enumerate(pdf_files, 1):
        pages, size = get_pdf_info(pdf_file)
        if pages:
            print(f"{i:2d}. {os.path.basename(pdf_file)}")
            print(f"    📁 路径: {pdf_file}")
            print(f"    📄 页数: {pages} 页")
            print(f"    💾 大小: {size:.1f} MB")
        else:
            print(f"{i:2d}. {os.path.basename(pdf_file)} (无法读取)")
        print()
    
    # 用户选择文件
    while True:
        try:
            choice = input(f"请选择要分割的PDF文件 (1-{len(pdf_files)}) 或输入 'q' 退出: ").strip()
            if choice.lower() == 'q':
                return
            
            choice = int(choice)
            if 1 <= choice <= len(pdf_files):
                selected_file = pdf_files[choice - 1]
                break
            else:
                print(f"❌ 请输入 1-{len(pdf_files)} 之间的数字")
        except ValueError:
            print("❌ 请输入有效的数字")
    
    # 获取分割参数
    print(f"\n📄 已选择: {os.path.basename(selected_file)}")
    
    # 设置每个文件的页数
    while True:
        try:
            pages_input = input("每个分割文件包含多少页？(默认50页，直接回车使用默认值): ").strip()
            if not pages_input:
                pages_per_file = 50
                break
            pages_per_file = int(pages_input)
            if pages_per_file > 0:
                break
            else:
                print("❌ 页数必须大于0")
        except ValueError:
            print("❌ 请输入有效的数字")
    
    # 设置输出目录
    default_output = f"output_{os.path.splitext(os.path.basename(selected_file))[0]}"
    output_dir = input(f"输出目录名称？(默认: {default_output}，直接回车使用默认值): ").strip()
    if not output_dir:
        output_dir = default_output
    
    # 确认分割
    print("\n📋 分割设置：")
    print(f"   📄 文件: {selected_file}")
    print(f"   📑 每个文件页数: {pages_per_file}")
    print(f"   📁 输出目录: {output_dir}")
    
    confirm = input("\n确认开始分割？(y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ 操作已取消")
        return
    
    # 执行分割
    success = split_pdf(selected_file, output_dir, pages_per_file)
    
    if success:
        print("\n🎉 PDF分割成功完成！")
    else:
        print("\n❌ PDF分割失败！")
    
    input("\n按回车键退出...")

if __name__ == "__main__":
    main()
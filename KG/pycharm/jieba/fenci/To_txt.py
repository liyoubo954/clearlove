import os
import re
import docx
import fitz
import pdfplumber
from pathlib import Path


def clean_text(text):
    """增强型数据清洗函数"""
    # 移除特殊符号和花纹字符
    cleaned = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s，。？！、：；“”‘’（）《》〈〉【】…—\-.,?!:;]', '', text)

    # 移除图表标注及内容（增强匹配）
    cleaned = re.sub(r'(图表?[\s\d]+[:：][\s\S]*?)(?=\n\S|\Z)', '', cleaned, flags=re.MULTILINE)

    # 移除页眉页脚（增强匹配）
    cleaned = re.sub(r'^(?:第[ \d]+页[ 共]*[ \d]*页?|\d{1,3}[-–—]\d{1,3}|机密|草稿|.*公司)$', '', cleaned,
                     flags=re.MULTILINE)

    # 移除网址和邮箱
    cleaned = re.sub(r'\b(?:https?://|www\.)\S+|\b\S+@\S+\.\S+\b', '', cleaned)

    # 标准化空白字符
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    return cleaned


def process_docx(input_path, output_path):
    """处理Word文档"""
    try:
        doc = docx.Document(input_path)
        full_text = [para.text for para in doc.paragraphs]
        text = '\n'.join(full_text)
        cleaned_text = clean_text(text)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
        return True
    except Exception as e:
        print(f"处理Word文档失败 {input_path}: {str(e)}")
        return False


def process_pdf(input_path, output_path):
    """处理PDF文档"""
    try:
        full_text = []

        # 使用pdfplumber提取文本
        with pdfplumber.open(input_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text.append(text)

        # 使用PyMuPDF补充提取
        with fitz.open(input_path) as doc:
            for page in doc:
                text = page.get_text()
                full_text.append(text)

        cleaned_text = clean_text('\n'.join(full_text))
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
        return True
    except Exception as e:
        print(f"处理PDF失败 {input_path}: {str(e)}")
        return False


def convert_folder(input_dir, output_dir):
    """批量转换文件夹"""
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    supported_files = {
        '.pdf': process_pdf,
        '.docx': process_docx
    }

    success = 0
    failed = 0

    for root, _, files in os.walk(input_dir):
        for file in files:
            src_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()

            if ext in supported_files:
                # 保持相对路径结构
                rel_path = os.path.relpath(root, input_dir)
                dest_folder = os.path.join(output_dir, rel_path)
                os.makedirs(dest_folder, exist_ok=True)

                dest_path = os.path.join(dest_folder,
                                         f"{os.path.splitext(file)[0]}.txt")

                # 执行转换
                if supported_files[ext](src_path, dest_path):
                    success += 1
                else:
                    failed += 1
            else:
                print(f"跳过不支持的文件: {file}")
                failed += 1

    print(f"\n转换完成！成功: {success} 个文件，失败: {failed} 个文件")


if __name__ == "__main__":
    input_folder = "F:\\ddg\\KG\\zhiwang"  # 原始文档文件夹
    output_folder = "F:\\ddg\\KG\\text"  # 输出文件夹

    convert_folder(input_folder, output_folder)
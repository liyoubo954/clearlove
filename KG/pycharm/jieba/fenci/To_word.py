import os
from pdf2docx import Converter
from tqdm import tqdm  # 进度条库，可选

def pdf_to_word(pdf_folder, word_folder):
    """
    将指定文件夹中的所有PDF转换为Word文档
    参数:
        pdf_folder: PDF文件所在文件夹路径
        word_folder: Word文件输出文件夹路径
    """
    # 创建输出文件夹
    if not os.path.exists(word_folder):
        os.makedirs(word_folder)

    # 获取所有PDF文件
    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]

    # 显示进度条（需要安装tqdm库，可选）
    for pdf_file in tqdm(pdf_files, desc="转换进度"):
        try:
            # 构建完整文件路径
            pdf_path = os.path.join(pdf_folder, pdf_file)
            word_path = os.path.join(word_folder, os.path.splitext(pdf_file)[0] + '.docx')

            # 转换文件
            cv = Converter(pdf_path)
            cv.convert(word_path, start=0, end=None)
            cv.close()

        except Exception as e:
            print(f"\n转换失败: {pdf_file} - {str(e)}")
            continue

    print(f"\n转换完成！共处理 {len(pdf_files)} 个文件，结果保存在：{word_folder}")

if __name__ == "__main__":
    # 设置路径（请修改为您的实际路径）
    pdf_folder = r"F:\\ddg\\KG\\zhiwang"    # PDF文件夹路径
    word_folder = r"F:\\ddg\\KG\\word"   # Word输出路径

    pdf_to_word(pdf_folder, word_folder)
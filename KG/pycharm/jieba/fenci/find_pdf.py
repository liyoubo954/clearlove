import os
import shutil

# 定义源文件夹路径（需要遍历的文件夹）
source_folder = r"F:\ddg\KG\file"

# 定义目标文件夹路径（存放PDF的新文件夹）
target_folder = r"F:\ddg\KG\zhiwang"


def copy_pdfs_to_folder(src_path, dst_path):
    """
    将源路径中的所有PDF复制到目标路径
    :param src_path: 需要遍历的源文件夹路径
    :param dst_path: 存放PDF的目标文件夹路径
    """
    # 创建目标文件夹（如果不存在）
    os.makedirs(dst_path, exist_ok=True)

    # 计数器
    copied_files = 0

    # 遍历源文件夹及其所有子文件夹
    for foldername, subfolders, filenames in os.walk(src_path):
        for filename in filenames:
            # 检查文件扩展名是否为PDF（不区分大小写）
            if filename.lower().endswith('.pdf'):
                # 构建完整文件路径
                src_file = os.path.join(foldername, filename)
                dst_file = os.path.join(dst_path, filename)

                # 处理重复文件名
                base_name, extension = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dst_file):
                    # 如果文件已存在，添加数字后缀
                    new_name = f"{base_name}({counter}){extension}"
                    dst_file = os.path.join(dst_path, new_name)
                    counter += 1

                # 复制文件
                shutil.copy2(src_file, dst_file)
                print(f"已复制: {src_file} -> {dst_file}")
                copied_files += 1

    print(f"\n操作完成！共复制 {copied_files} 个PDF文件。")


# 执行复制操作
if __name__ == "__main__":
    copy_pdfs_to_folder(source_folder, target_folder)
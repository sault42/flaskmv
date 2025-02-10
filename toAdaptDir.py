import os
import shutil

def move_files_to_parent(directory):
    # 遍历一级子目录
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        print(f"Processing: {subdir_path}")
        # 确保是目录
        if os.path.isdir(subdir_path):
            # 遍历子目录中的所有文件和子目录
            for root, dirs, files in os.walk(subdir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    target_path = os.path.join(subdir_path, file)
                    
                    # 如果目标文件已存在，则重命名文件
                    if os.path.exists(target_path):
                        base, extension = os.path.splitext(file)
                        counter = 1
                        while os.path.exists(target_path):
                            target_path = os.path.join(subdir_path, f"{base}_{counter}{extension}")
                            counter += 1
                    
                    # 移动文件
                    shutil.move(file_path, target_path)
                    print(f"Moved: {file_path} -> {target_path}")
                
                # 删除空目录（除了当前一级子目录）
                if root != subdir_path and not os.listdir(root):
                    os.rmdir(root)
                    print(f"Removed empty directory: {root}")

# 示例用法
move_files_to_parent('assets/images')
import os
import shutil

# 源目录（包含所有子文件夹的根目录）
src_root = 'E:\\F'
# 目标目录（所有文件移动到这里）
dst_root = 'E:\\F\\0\\all_files'


def move_files(src, dst):
    # 遍历所有子目录
    for root, dirs, files in os.walk(src):
        # 跳过目标目录本身
        if root.startswith(dst):
            continue
        
        for file in files:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst, file)
            
            # 处理重名文件
            counter = 1
            while os.path.exists(dst_path):
                filename, extension = os.path.splitext(file)
                dst_path = os.path.join(dst, f"{filename}_{counter}{extension}")
                counter += 1
            
            # 移动文件并打印日志
            shutil.move(src_path, dst_path)
            print(f'已移动: {src_path} -> {dst_path}')

if __name__ == '__main__':
    # 确保目标目录存在
    os.makedirs(dst_root, exist_ok=True)
    
    # 从源目录根开始处理
    move_files(src_root, dst_root)
    print('所有文件移动完成！')
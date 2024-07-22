import os
import random

# 设置随机种子以确保可重复性
random.seed(42)

# 数据集路径
dataset_path = r'D:\Desktop\PCB_Detect\yolov10-main\datasets\VOC'

# 图像和注释文件夹
image_folder = os.path.join(dataset_path, 'JPEGImages')

# 获取所有图像文件名（不带扩展名）
all_files = [f.split('.')[0] for f in os.listdir(image_folder) if f.endswith('.jpg')]

# 打乱所有文件
random.shuffle(all_files)

# 划分比例
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# 计算每个集合的大小
total_files = len(all_files)
train_size = int(train_ratio * total_files)
val_size = int(val_ratio * total_files)
test_size = total_files - train_size - val_size

# 划分数据集
train_files = all_files[:train_size]
val_files = all_files[train_size:train_size + val_size]
test_files = all_files[train_size + val_size:]

# 保存文件列表
def save_list(file_list, file_path):
    with open(file_path, 'w') as f:
        for file in file_list:
            f.write(f'datasets/VOC/JPEGImages/{file}.jpg\n')

# 确保目录存在
output_dirs = [
    os.path.join(dataset_path, 'ImageSets/Main'),
]

for output_dir in output_dirs:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

# 保存训练、验证、测试文件列表
save_list(train_files, os.path.join(dataset_path, 'ImageSets/Main/train.txt'))
save_list(val_files, os.path.join(dataset_path, 'ImageSets/Main/val.txt'))
save_list(train_files + val_files, os.path.join(dataset_path, 'ImageSets/Main/trainval.txt'))
save_list(test_files, os.path.join(dataset_path, 'ImageSets/Main/test.txt'))

print("Data split and files saved successfully.")

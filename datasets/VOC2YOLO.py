import os
import xml.etree.ElementTree as ET

# Pascal VOC 数据集路径
voc_dataset_path = r'D:\Desktop\PCB_Detect\yolov10-main\datasets\VOC'

# YOLO 数据集标签路径
yolo_labels_path = r'D:\Desktop\PCB_Detect\yolov10-main\datasets\VOC\labels'

# 类别名称
class_names = ['missing_hole', 'mouse_bite', 'open_circuit', 'short', 'spur', 'spurious_copper']

# 创建YOLO标签文件夹
if not os.path.exists(yolo_labels_path):
    os.makedirs(yolo_labels_path)

# 获取所有XML文件
annotation_files = [f for f in os.listdir(os.path.join(voc_dataset_path, 'Annotations')) if f.endswith('.xml')]

# 解析每个XML文件并生成YOLO格式标签
for annotation_file in annotation_files:
    tree = ET.parse(os.path.join(voc_dataset_path, 'Annotations', annotation_file))
    root = tree.getroot()
    
    image_id = os.path.splitext(annotation_file)[0]
    yolo_label_file = os.path.join(yolo_labels_path, f'{image_id}.txt')
    
    with open(yolo_label_file, 'w') as f:
        for obj in root.findall('object'):
            class_name = obj.find('name').text
            if class_name not in class_names:
                continue
            
            class_id = class_names.index(class_name)
            
            bndbox = obj.find('bndbox')
            xmin = float(bndbox.find('xmin').text)
            ymin = float(bndbox.find('ymin').text)
            xmax = float(bndbox.find('xmax').text)
            ymax = float(bndbox.find('ymax').text)
            
            # 获取图像尺寸
            width = float(root.find('size/width').text)
            height = float(root.find('size/height').text)
            
            # 计算YOLO格式的边界框参数
            x_center = (xmin + xmax) / 2.0 / width
            y_center = (ymin + ymax) / 2.0 / height
            bbox_width = (xmax - xmin) / width
            bbox_height = (ymax - ymin) / height
            
            f.write(f'{class_id} {x_center} {y_center} {bbox_width} {bbox_height}\n')

from ultralytics import YOLOv10
import torch

# 从预训练权重加载模型
model = YOLOv10.from_pretrained('jameslahm/yolov10m')

# 设置设备
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# 训练配置
data_yaml = 'VOC.yaml'
epochs = 500
batch_size = 128
img_size = 640

if __name__ == '__main__':
    # 开始训练
    model.train(
        data=data_yaml,
        epochs=epochs,
        batch=batch_size,
        imgsz=img_size
    )

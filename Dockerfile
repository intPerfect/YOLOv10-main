# 使用 Python 3.9 精简版作为基础镜像
FROM python:3.9-slim-buster

# 更新软件包列表并安装必需的 Linux 包，尝试修复丢失的包
RUN apt-get update --fix-missing \
    && apt-get install --fix-missing --no-install-recommends -y \
        gcc \
        git \
        zip \
        curl \
        htop \
        libgl1 \
        libglib2.0-0 \
        libpython3-dev \
        gnupg \
        g++ \
        libusb-1.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安装安全更新
RUN apt-get upgrade --no-install-recommends -y openssl tar

# 将当前目录下的所有文件复制到容器的 /yolov10-main 目录中
ADD . /yolov10-main
# 设置工作目录为 /yolov10-main
WORKDIR /yolov10-main

# 安装 PyTorch 以及依赖包
RUN pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cu118
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 设置容器启动时执行的默认命令
CMD ["python", "train.py"]

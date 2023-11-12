import os
from PIL import Image

def get_latest_image(path, file_extension='.png'):
    # 获取路径下所有指定格式的文件，并带上它们的创建时间
    images = [(f, os.path.getctime(os.path.join(path, f))) for f in os.listdir(path) if f.endswith(file_extension)]

    if not images:
        return None

    # 根据创建时间排序，获取最新的一个文件
    latest_image_file = max(images, key=lambda x: x[1])[0]

    # 读取并返回这个最新的图片
    return Image.open(os.path.join(path, latest_image_file))

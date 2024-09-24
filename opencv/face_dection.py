

import cv2
import base64
from aip import AipFace

# 读取图片
image_path = 'D:\\桌面\\文档\\me.jpg'
with open(image_path, 'rb') as f:
    image_data = f.read()

# 将图片数据转换为Base64编码
image_base64 = base64.b64encode(image_data).decode()

# 替换成你的API Key和Secret Key
API_KEY = 'ecW6gKrtvkFqzt4eFGYws6gT'
SECRET_KEY = 'u2VFZJnzgkugp3LFWm3eisDXsk9P9CAx114002982'
APP_ID = '114002982'

# 初始化AipFace对象
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 调用人脸检测API
options = {
    "face_field": "age,gender,expression,beauty,faceshape,facetype,glasses,landmark,race,quality,faceliveness"
}
result = client.detect(image_base64, image_type='BASE64', options=options)

# 打印结果
print(result)
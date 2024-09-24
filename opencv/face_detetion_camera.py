# 照片进行人脸识别
import cv2
import numpy as np


cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error!")
    exit()
# 加载 Haar 级联分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:


    # 读取一帧图像
    ret, frame = cap.read()
    if not ret:
        print("Error!")
        break

# 检查图像是否正确加载
    if frame is None:
        print("Error: Could not load image.")
        exit()

    # 转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测图像中的人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 在检测到的人脸周围画矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 显示结果
    cv2.imshow('Face Detection', frame)

    # 按任意键关闭窗口
    if cv2.waitKey(1) & 0xFF == ord('1'):
        break

cv2.destroyAllWindows()
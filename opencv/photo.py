# opencv开启usb摄像头连接
import cv2
import numpy as np

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error!")
    exit()
while True:
    ret, frame = cap.read()
    # 从摄像头读取一帧图像。ret
    # 是一个布尔值，表示是否成功读取帧，frame
    # 是读取到的帧。
    if not ret:
        print("Error!")
        break

    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0XFF == ord('1'):
        break
    print(frame, ret)
cap.release()
cv2.destroyAllWindows()
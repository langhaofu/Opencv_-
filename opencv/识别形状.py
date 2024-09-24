import cv2
import numpy as np

# 打开摄像头
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error!")
    exit()

while True:
    # 读取一帧图像
    ret, frame = cap.read()
    if not ret:
        print("Error!")
        break

    # 转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 边缘检测
    edges = cv2.Canny(gray, 50, 150)

    # 查找轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # 轮廓近似
        epsilon = 0.2 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # 根据顶点数识别形状
        if len(approx) == 4:
            # 检查轮廓是否为近似矩形
            shape = "Square" if cv2.isContourConvex(approx) else "Rectangle"
        elif len(approx) == 3:
            shape = "Triangle"
        elif len(approx) > 4:
            shape = "Circle"  # 假设所有非四边形的多边形都是圆形
        else:
            continue

        # 绘制轮廓和形状名称
        cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3)
        cv2.putText(frame, shape, (cnt[:, 0, 0].min(), cnt[:, 0, 1].min()), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    # 显示结果
    cv2.imshow('Shape Detection', frame)

    # 按 '1' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('1'):
        break

# 释放摄像头资源
cap.release()
# 关闭所有 OpenCV 窗口
cv2.destroyAllWindows()
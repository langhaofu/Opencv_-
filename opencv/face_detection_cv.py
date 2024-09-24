#照片进行人脸识别
import cv2

# 加载 Haar 级联分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

# 读取图像
image = cv2.imread('G:\\pycharm\\projects\\opencv\\opencv\\me.jpg')

# 检查图像是否正确加载
if image is None:
    print("Error: Could not load image.")
    exit()

# 转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 检测图像中的人脸
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 在检测到的人脸周围画矩形框
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 显示结果
cv2.imshow('Face Detection', image)

# 按任意键关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
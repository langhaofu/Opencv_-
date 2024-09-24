import cv2

image_path = "G:\\pycharm\\projects\\opencv\\opencv\\jiege.jpg"
image = cv2.imread(image_path)

# if image is None:
#     print("Error: Image not found")
# else:
#     print("Image loaded successfully")
#     cv2.imshow('love', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
resized_image = cv2.resize(image, (300, 300))
cv2.imwrite('G:\\pycharm\\projects\\opencv\\opencv\\resized_image.jpg', resized_image)
# 缩放图片
scaled_image = cv2.resize(image,(400, 400))
# 旋转图像
# rotated_image = cv2.warpAffine(image, 90, (480, 480))
# 裁剪图像
x, y, w, h = 100, 100, 200, 200
cropped_image = image[y:y+h, x:+w]
# 转换成灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 滤波
# 高斯滤波
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
# 边缘检测 好帅
edges = cv2.Canny(image, 100, 200)
cv2.imshow('rotated_image', edges)
cv2.waitKey(0)
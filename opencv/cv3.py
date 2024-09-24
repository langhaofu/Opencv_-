import cv2
import numpy as np

# 读取图像
image = cv2.imread('G:\\pycharm\\projects\\opencv\\opencv\\jiege.jpg')

# 定义源图像中的三个点
src_points = np.float32([[50, 50], [200, 50], [50, 200]])

# 定义目标图像中的三个点，这些点定义了源点应该映射到的位置
dst_points = np.float32([[10, 100], [200, 100], [100, 250]])

# 计算仿射变换矩阵
affine_matrix = cv2.getAffineTransform(src_points, dst_points)

# 应用仿射变换
transformed_image = cv2.warpAffine(image, affine_matrix, (image.shape[1], image.shape[0]))

# 显示结果
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
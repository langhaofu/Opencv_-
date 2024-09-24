import cv2

image_path = "G:\\pycharm\\projects\\opencv\\opencv\\jiege.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")
    cv2.imshow('love', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imwrite('G:\\pycharm\\projects\\opencv\\opencv\\image_rgb.jpg', image_rgb)

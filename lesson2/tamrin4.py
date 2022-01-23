import cv2
import numpy as np
images = []
for i in range(0, 14):
    img = cv2.imread(f"image_o/h{i}.jpg", 0)
    images.append(img)
    rows, cols = img.shape
result = np.zeros((rows, cols), dtype="uint8")
for image in images:
    result += image // 14
cv2.imshow("Out_Put", result)
cv2.waitKey()
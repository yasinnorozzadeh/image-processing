import cv2
import numpy as np
images = [[0 for i in range(5)] for j in range(4)]
for i in range(4):
    for j in range(5):
        images[i][j] = cv2.imread(f"{i+1}/{j+1}.jpg" , 0)
        images[i][j] = cv2.resize(images[i][j], (400, 400))
image_without_noise = [0 for i in range(4)]
for i in range(4):
    for j in range(5):
        image_without_noise[i] += (images[i][j] // 5)
img = np.zeros((800, 800), dtype= np.uint8)
img[0:400, 0:400] = image_without_noise[0]
img[0:400, 400:800] = image_without_noise[1]
img[400:800, 0:400] = image_without_noise[2]
img[400:800, 400:800] = image_without_noise[3]
cv2.imshow("Out_Put", img)
cv2.waitKey()

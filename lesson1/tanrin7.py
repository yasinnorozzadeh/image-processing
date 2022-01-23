import cv2
import numpy as np
img = np.arange(0, 1 , 1, np.uint8)
img = np.resize(img , (250 , 250))
h, w = img.shape
for i in range (h):
    for j in range(w):
        img[i,j]= i - 255 
cv2.imshow("🐱‍👤" , img)
cv2.waitKey()
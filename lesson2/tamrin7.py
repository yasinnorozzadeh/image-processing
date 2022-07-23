import cv2
import random
import numpy as np
img=cv2.imread("Assignment22/hw2/chess pieces.jpg" , 0)
img1=cv2.imread("Assignment22/hw2/chess pieces.jpg" , 0)
h ,w =img.shape
for i in range(h):
    for j in range(w):
        r = random.random()
        if r < 0.06:
            img[i][j] = random.randint(100,255)
cv2.imshow("Out_Put" , img)
cv2.waitKey()

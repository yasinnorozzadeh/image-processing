import cv2
import numpy as np
import cv2
import array
img = cv2.imread('3.jpg')
imge = cv2.resize(img, (700, 600))
h, w = imge.shape[:2]
center = w/2, h/2
img2 = cv2.getRotationMatrix2D(center, 180, 1)
imgr = cv2.warpAffine(imge, img2, (w, h))
cv2.imshow('result', imgr)
cv2.waitKey()

import cv2
img1 = cv2.imread("Assignment22/hw2/a.tif", 0)
img2 = cv2.imread("Assignment22/hw2/b.tif", 0)
result = img2 - img1
cv2.imshow("Out_Put", result)
cv2.waitKey()
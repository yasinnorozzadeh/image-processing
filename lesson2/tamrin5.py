import cv2

img1 = cv2.imread("r.jpg", 0)
img2 = cv2.imread("s.jpg", 0)
img_1 = cv2.resize(img1, (600, 600))
img_2 = cv2.resize(img2, (600, 600))
# result = img_1//2 + img_2//6
result = img_1//4 + img_2//2
cv2.imshow("Out_Put", result)
cv2.waitKey()
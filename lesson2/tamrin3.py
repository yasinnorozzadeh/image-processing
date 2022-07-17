import cv2
img1 = cv2.imread("Assignment22/hw2/board - test.bmp", 0)
img2 = cv2.imread("Assignment22/hw2/board - origin.bmp", 0)
img_1 = cv2.resize(img1, (800, 800))
img_2 = cv2.resize(img2, (800, 800))
img__2 = cv2.flip(img_2, 1)
sub_imgs = cv2.subtract(img__2, img_1)
result1 = sub_imgs
cv2.imshow("output1", result1)
result = sub_imgs * 255
h,w= result.shape
for i in range(h):
    for j in range(w):
        if result[i][j] < 0:
            result[i][j] = 0
        elif result[i][j] > 255:
            result[i][j] = 255
cv2.imshow("Out_Put", result)
cv2.waitKey()

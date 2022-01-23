import cv2

img = cv2.imread("poster.jpg", 0)

cv2.imwrite("result.jpg", img)
print(img.shape)
treshold = 180
height, width = img.shape

for i in range(250):
    if i <= 100:
        for j in range(100-i, 250-i):
            if j >= 0:
                img[i, j] = 0
    else:
        for j in range(0, 250-i):
            if j >= 0:
                img[i, j] = 0

img[0:600, 0:40] = 0
img[560:600, 0:541] = 0
img[0:600, 501:541] = 0
img[0:40, 0:541] = 0



print(img)

cv2.imshow("output", img)
cv2.waitKey()


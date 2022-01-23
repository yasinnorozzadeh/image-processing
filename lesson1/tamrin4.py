import cv2

img = cv2.imread("4.jpg", 0)
cv2.imwrite("result.jpg", img)
print(img.shape)
img =cv2.resize(img,(600, 600))
treshold = 180
height, width = img.shape

for i in range(height):
    for j in range(width):
        if img[i, j] > treshold:
            img[i, j] = 255
        else:
            img[i, j] = 0

print(img)
cv2.imshow("output", img)
cv2.waitKey()

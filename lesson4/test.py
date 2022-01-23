import cv2
import numpy as np
    

image = np.zeros((500, 500), dtype="uint8")

points = np.array([(100, 50),
                   (400, 250),
                   (150, 200),
                   (300, 350)])


cv2.drawContours(image, [points], -1, (255, 255, 255), -1)

cv2.imshow("out_put", image)
cv2.waitKey()
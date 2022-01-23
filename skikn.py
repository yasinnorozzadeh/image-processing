import cv2
import numpy as np

lower = np.array([0, 55, 75])
upper = np.array([10, 90, 200])
video = cv2.VideoCapture(0)
while True:
    _,frame = video.read()
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    skin = cv2.inRange(frame_hsv, lower, upper)    

    skin = cv2.bitwise_and(frame, frame,mask=skin)
    cv2.imshow("output",skin)
    if cv2.waitKey(1)==ord("q"):
        break
video.release()

import cv2
# import numpy as np

cap = cv2.VideoCapture(0)
pixels_list = []
row=1
while True:
    ret,frame = cap.read()
    width , height, _ = frame.shape
    # width , height = frame.shape
    if not ret:
        break
    if cv2.waitKey(1) == ord("q"):
        break
    cv2.line(frame,(0,row),(height,row),(50,100,150))
    pixels_list.append(frame[row-1])
    frame[:row] = pixels_list
    row += 1
    if row>width:
        cv2.imwrite("filter.jpg",frame)
        row=1
        pixels_list.clear()
    cv2.imshow("Filter",frame)

cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2
video_cap = cv2.VideoCapture(0)
size_text = 1.5

while True:
    ret, frame = video_cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    width, height = frame_gray.shape
    
    target = frame_gray[(width//8)*3:(width//8)*5, (height//8)*3:(height//8)*5]

    kernel = np.ones((45, 45), np.float32)/2025
    frame_gray = cv2.filter2D(frame_gray, -1, kernel, borderType=cv2.BORDER_CONSTANT)

    alpha = -3
    beta = -100
    enhanced_target = cv2.convertScaleAbs(target, alpha=alpha, beta=beta)

    frame_gray[(width//8)*3:(width//8)*5, (height//8)*3:(height//8)*5] = enhanced_target
    cv2.rectangle(frame_gray, (height//8*3, width//8*3), ((height//8*5), (width//8*5)), (0, 0, 0), 4)
    color_me = np.average(enhanced_target)
    if size_text <= 0:
        break
    if  0 < np.average(color_me) <= 85:
        cv2.rectangle(frame,(300,200), (400,300), (0, 0, 0),2)
        cv2.putText(frame,'Black',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),int(size_text))
        size_text += 0.1
    elif 85 < np.average(color_me) <= 170:
        cv2.rectangle(frame,(300,200), (400,300), (127, 127, 127),2)
        cv2.putText(frame,'gray',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,127,127),int(size_text))
        size_text == 2.5
    elif 170 < np.average(color_me) <= 255:
        cv2.rectangle(frame,(300,200), (400,300), (255, 255, 255),2)
        cv2.putText(frame,'white',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 255),int(size_text))
        size_text -= 0.1
    cv2.imshow("cam-0", frame_gray)

video_cap.release()
cv2.destroyAllWindows()

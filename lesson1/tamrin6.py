import numpy as np
import cv2
width=hight=600
firstchn = np.zeros((width, hight), np.uint8)
firstchn [:,:] = 0
firstchn[150:400] = 255
firstchn[180:200, 120:160] = 0
firstchn[200:220, 140:180] = 0
firstchn[220:240, 160:200]= 0

firstchn[240:260, 180:260]= 0

firstchn[220:240, 240:280]= 0
firstchn[200:220, 260:300]= 0
firstchn[180:200, 280:320]= 0

firstchn[260:340, 200:240]= 0


cv2.imshow('Y', firstchn)
cv2.waitKey()
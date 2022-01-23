import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
from imutils.perspective import four_point_transform 

parser = argparse.ArgumentParser(description='yasin sudoku detector')
parser.add_argument('--filter_siz', type=int, help='size of GaussianBlur mask', default=7)
args = parser.parse_args()

video = cv2.VideoCapture(0)

while True:

    ret, frame = video.read()

    if not ret:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    thresh = cv2.GaussianBlur(frame, (args.filter_siz, args.filter_siz), 3)
    thresh = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0]
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    sudoku_contour = None

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            sudoku_contour = approx
            break
    
    if sudoku_contour is None:
        print("I can not find Sudoku ")
    else:
        cv2.drawContours(frame, [sudoku_contour], -1, (0, 255, 255), 20)
        crop = four_point_transform(frame, approx.reshape(4,2))
        crop = cv2.resize(crop, (500, 500))
        cv2.imshow('result', frame)
        if cv2.waitKey(1) == ord('s'):
            cv2.imwrite("sudoku.jpg", crop)
            
    if cv2.waitKey(1) == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()

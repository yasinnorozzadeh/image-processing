import cv2
import numpy as np
width=height=1600
board = np.zeros((width,height), dtype=np.uint16)
color=255
for i in range(0,1600,100):
    count=0
    for j in range(0,height,100):
        if color == 255:
            if count % 2 == 0:
                board[i:i+100,j:j+100] = 255
        else:
            if count % 2 != 0:
                board[i:i + 100, j:j + 100] = 255
        count+=1
    if color == 255:
        color = 0
    else:
        color = 255
# print(board)
cv2.imwrite('chess-Bord.jpg',board)
cv2.waitKey()

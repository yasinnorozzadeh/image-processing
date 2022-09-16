import cv2
import numpy as np


cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = cv2.resize(frame, (800, 800))
    width, height, _ = frame.shape
    blur = cv2.blur(frame,(50,50))
    rectangle = frame[(width//2)-100:(width//2)+100,(height//2)-100:(height//2)+100]
    blur[(width//2)-100:(width//2)+100,(height//2)-100:(height//2)+100] = rectangle

    R = int(np.mean(rectangle[:,:,2]))
    G = int(np.mean(rectangle[:,:,1]))
    B = int(np.mean(rectangle[:,:,0]))
    
    if 150 < R <= 255 and 150 < G <= 255 and 150 < B <= 255:
        rgb_color = "White"
    elif 0 <= R <= 100 and 0 <= G <= 100 and 0 <= B <= 100:
        rgb_color = "Black"
    elif 101 <= R <= 149 and 101 <= G <= 149 and 101 <= B <= 149:
        rgb_color = "Gray"
    elif 0 <= R <= 100 and 0 <= G <= 100 and 100 <= B <= 255:
        rgb_color = "Blue"
    elif 100 <= R <= 200 and 0 <= G <= 100 and 0 <= B <= 100:
        rgb_color = "Red"
    elif 0 <= R <= 50 and 100 <= G <= 150 and 0 <= B <= 150:
        rgb_color = "Green"
    elif 90 <= R <= 150 and 90 <= G <= 150 and 120 <= B <= 200:
        rgb_color = "Magenta"
    elif 100 <= R <= 255 and 100 <= G <= 255 and 0 <= B <= 100:
        rgb_color = "Yellow"
    elif 0 <= R <= 100 and 100 <= G <= 150 and 100 <= B <= 200:
        rgb_color = "Cyan"
  
    cv2.putText(blur,f"R: {str(R)}, G: {str(G)}, B: {str(B)}",(10,40),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(G,R,B),2)
    cv2.putText(blur,f"Color: {rgb_color}",(10,70),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(B,G,R),2)  
    cv2.imshow("frame", blur)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
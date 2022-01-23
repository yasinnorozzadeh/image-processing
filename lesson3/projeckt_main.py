import cv2
import cvzone
import keyboard


f_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
e_detector = cv2.CascadeClassifier("haarcascade_eye.xml")
s_detector = cv2.CascadeClassifier("haarcascade_smile.xml")
f_emoj = cv2.imread("glass.png", cv2.IMREAD_UNCHANGED)
e_Emoj = cv2.imread("eye.png", cv2.IMREAD_UNCHANGED)
s_Emoj = cv2.imread("smile.png", cv2.IMREAD_UNCHANGED)

video_cap = cv2.VideoCapture(0)
current_state = 0
while True:    
    ret, frame = video_cap.read()
    if ret == False:
        break

    cv2.putText(frame, "^_^", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    k = cv2.waitKey(1)
    if keyboard.is_pressed('1'):
        FACES = f_detector.detectMultiScale(frame, 1.3)
        for (x, y, w, h) in FACES:
            finalEmojy = cv2.resize(f_emoj, (w, h))
            frame = cvzone.overlayPNG(frame, finalEmojy, [x, y])

    if keyboard.is_pressed('2'):
        LEYE = e_detector.detectMultiScale(frame, 2, maxSize=(50,50))
        for (x, y, w, h) in LEYE:
            finalEmojy = cv2.resize(e_Emoj, (w, h))
            frame = cvzone.overlayPNG(frame, finalEmojy, [x, y])  
        SMILE = s_detector.detectMultiScale(frame, 1.3, 15)
        for (x, y, w, h) in SMILE:
            finalEmojy = cv2.resize(s_Emoj, (w, h))
            frame = cvzone.overlayPNG(frame, finalEmojy, [x, y])
            
    if keyboard.is_pressed('3'):
        FACES = f_detector.detectMultiScale(frame, 1.3)
        for (x, y, w, h) in FACES:            
            blurred = frame[y:y+h, x:x+w]
            pixlated = cv2.resize(blurred, (15, 15), interpolation=cv2.INTER_LINEAR)
            output = cv2.resize(pixlated, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = output

    if keyboard.is_pressed('4'):
        FACES = f_detector.detectMultiScale(frame, 1.3)
        for (x, y, w, h) in FACES:
            blurred = cv2.GaussianBlur(frame[y:y+h, x:x+w], (25, 25), 35)
            frame[y:y+h, x:x+w] = blurred

    if keyboard.is_pressed('esc'):
        exit()

    cv2.imshow("Out_Put", frame)

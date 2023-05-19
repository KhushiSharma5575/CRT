import numpy as np
import cv2
from time import sleep
fd= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
vid= cv2.VideoCapture(0)

while True:
    flag , img = vid.read()
    if flag:
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        x1,y1,w,h=(200,400,200,200)
        
        faces = fd.detectMultiScale(img_grey,1.1,5)
        for x1,y1,w,h in faces:
            cv2.rectangle(
                img,
                pt1=(x1,y1), pt2=(x1+w, y1+h),
                color=(0,0,255),thickness=10
            )
        
        cv2.imshow('Preview' ,img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows() 
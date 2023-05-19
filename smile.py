import numpy as np
import cv2
from time import sleep
fd = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
sd = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
vid= cv2.VideoCapture(0)
seq=0
old_seq=0
captured =False
while not captured:
    flag , img = vid.read()
    if flag:
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        x1,y1,w,h=(200,400,200,200)
        
        faces = fd.detectMultiScale(
            img_grey,
            scaleFactor = 1.1,
            minNeighbors=5,
            minSize= (180,180))
        
        
        for x1,y1,w,h in faces:
            face = img_grey[y1:y1+h, x1:x1+w].copy()
            smile = sd.detectMultiScale( face, 1.1, 5, minSize=(50,50))
            
            if len(smile) ==1:
                seq += 1
                if seq==5:
                    captured= cv2.imwrite('2.png', img)
                    break
                xs,ys,ws,hs= smile[0]
                cv2.rectangle(
                img,
                pt1=(xs+x1,ys+y1), pt2=(xs+x1+ws, ys+y1+hs),
                color=(0,0,255),thickness=5
                )
            else:
                seq=0
        
            cv2.rectangle(
                 img,
                 pt1=(x1,y1), pt2=(x1+w, y1+h),
                 color=(0,255,0),thickness=3
                
            )
        
        cv2.imshow('Preview' ,img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        cv2.imwrite('2.png', img)
    else:
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows() 


#import cv2

# video = cv2.VideoCapture(0)
# faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")
# smileCascade = cv2.CascadeClassifier("dataset/haarcascade_smile.xml")

# while True:
#     success,img = video.read()
#     grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(grayImg,1.1,4)
#     cnt=1
#     keyPressed = cv2.waitKey(1)

#     for x,y,w,h in faces:
#         img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)
#         smiles = smileCascade.detectMultiScale(grayImg,1.8,15)
#         for x,y,w,h in smiles:
#             img = cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),5)
#             print("Image "+str(cnt)+"Saved")
#             path=r'C:\Users\BOSS\Desktop\SmileCapture\images\img'+str(cnt)+'.jpg'
#             cv2.imwrite(path,img)
#             cnt +=1
#             if(cnt>=2):    
#                 break
                
#     cv2.imshow('live video',img)
#     if(keyPressed & 0xFF==ord('q')):
#         break

# video.release()                                  
# cv2.destroyAllWindows()
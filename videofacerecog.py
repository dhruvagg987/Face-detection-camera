import cv2, time
import numpy as np

video=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("D:/haarcascade_frontalface_default.xml")

while True:
    check,frame=video.read()
    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.05,5)
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("frames",frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()

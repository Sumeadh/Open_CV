import numpy as np
import cv2 as cv
'''
cap=cv2.VideoCapture(0)
while True:
    r,frame=cap.read()
    hsv1 = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv3 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('original', frame) #give different names in the 1st arg block for the code to show 4 vids
    cv2.imshow('show video',hsv1)
    cv2.imshow('show ', hsv3)
    cv2.imshow('video', hsv2)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
'''

cap=cv.VideoCapture('City_Roam.mp4')
r,frame1=cap.read()
r,frame2=cap.read()

while cap.isOpened():
    diff=cv.absdiff(frame1,frame2)
    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),0)
    #cv.imshow('grayimage',blur)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated=cv.dilate(thresh,None,3)
    contours,_=cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

    for i in contours:
        (x,y,z,k)=cv.boundingRect(i)
        if cv.contourArea(i)<1000:
            continue
        cv.rectangle(frame1,(x,y),(x+z,y+k),(255,0,0),2)
        cv.drawContours(frame1,i,-1,(0,255,0),1)
    cv.imshow('finalOutput',frame1)
    frame1=frame2
    r,frame2=cap.read()
    if cv.waitKey(100) & 0xFF==ord('n'):
        break
cap.release()
cv.destroyAllWindows()

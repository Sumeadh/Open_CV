import cv2
import numpy as np

#Creating canvas
img=np.zeros((500,600,3))

cap=cv2.VideoCapture(0)

while (cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    
    hsvframe=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #Converting the capture into hsv for segmentation
    lower_blue=np.array([94, 80, 2])
    upper_blue=np.array([120, 255, 255])
    mask=cv2.inRange(hsvframe,lower_blue,upper_blue) #Masking
    cv2.imshow("Masked image",mask)
    #Finding the contour
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    
    max_contour = contours[0] #Defining max contour as we get error if we use contour
    for i in contours:
        if cv2.contourArea(i)>cv2.contourArea(max_contour):
            max_contour=i
    M=cv2.moments(max_contour)
    if M['m00']!=0:
        cx=int(M['m10']/M['m00']) #Standard formula for calculating centre of object 
        cy=int(M['m01']/M['m00'])
        cv2.drawContours(frame,max_contour,-1,(0,255,0),2)
        cv2.circle(frame,(cx,cy),7,(0,0,255),2)
        cv2.putText(frame,"DUMBASS",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
        cv2.circle(img, (cx, cy), 7, (0, 0, 255), -1)

    cv2.imshow('Contours',frame)
    cv2.imshow('Target',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
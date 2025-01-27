import cv2 as cv
import numpy as np

#callback function for trackbar, plays no role
def nothing(x):
    pass
'''
cap1= cv.VideoCapture(0)
cap2=cv.VideoCapture(0)
#window for trackbar
cv.namedWindow("Trackbar")
cv.createTrackbar('value','Trackbar',0,255,nothing)

while (cap1.isOpened()):
    ret,frame=cap1.read()
    if ret == True :        
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#contours works properly on one scale     
       

        x = cv.getTrackbarPos('value','Trackbar') #getting trackbar value
        ret1, thresh1 = cv.threshold(gray, x, 255, cv.THRESH_BINARY)#binary thresholding 
 

        contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        #print('contours',len(contours),'heirarchy',len(hierarchy))
        cv.drawContours(frame, contours, -1, (0, 255, 0), 3)  
     
        cv.imshow("Binary Thresholding",thresh1)
        cv.imshow("Contours",frame)
        
        
    if cv.waitKey(25) & 0xFF == ord('q'): #escape on entering q
        break


    
while :
    
    if ret1 == True:
        
        x = cv.getTrackbarPos('value', 'Trackbar')  # getting trackbar value
       


        
    if cv.waitKey(25) & 0xFF == ord('q'):  # escape on entering q
        break

cap1.release()
cap2.release()
cv.destroyAllWindows()
'''
# [Next, Previous, First_Child, Parent]
img = cv.imread( r'C:\Users\Sumeadh\Desktop\PROGRAMS\OPEN CV\contours_hierarchy.png')
cv.imshow('orginal image', img)
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
r,threshHold=cv.threshold(gray_img,127,255,cv.THRESH_BINARY)
contours,heirarchy=cv.findContours(threshHold,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(heirarchy)
cntr=cv.drawContours(threshHold,contours,7,(255,0,255),5)
cv.imshow('contours',cntr)
cv.waitKey(0)
cv.destroyAllWindows()
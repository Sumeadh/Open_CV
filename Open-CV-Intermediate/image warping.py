import cv2
import numpy as np
cnt=0
arr=np.zeros((4,2),int)
def click(event,x,y,flags,param):
    global cnt
    if event==cv2.EVENT_LBUTTONDOWN:
        arr[cnt]=x,y
        cnt+=1
        print(x,y)
        
img=cv2.imread('image.png')
img=cv2.resize(img,(500,500))


while True:
    if cnt==4:
       pts1=np.float32([arr[0],arr[1],arr[2],arr[3]])
       pts2=np.float32([[0,0],[500,0],[0,500],[500,500]])
       matrix=cv2.getPerspectiveTransform(pts1,pts2)
       final=cv2.warpPerspective(img,matrix,(500,500))
       cv2.imshow('Output',final)
       break
    cv2.namedWindow('Input')
    cv2.setMouseCallback('Input',click)
    cv2.imshow('Input',img)
    cv2.waitKey(1)
 
    
    


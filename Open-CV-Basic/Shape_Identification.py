import cv2
import numpy as np
img = cv2.imread('shapes.jpeg')
#print(np.shape(img))
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('Gray.jpeg',grey)
img_gray = cv2.imread('gray.jpeg')
_, thresh = cv2.threshold(grey, 245, 255, cv2.THRESH_BINARY)
cv2.imshow('thresholded image',thresh)
contours, _ = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, 0, (0, 255, 0), 5)
print(_)

for count, contour in enumerate(contours,0):
    if count>0:
        approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)#
        #print(approx)
        #print(np.shape(approx))
        cv2.drawContours(img, [approx],0,(0, 255, 0), 2)
        x=approx.ravel()[0]#
        print(approx)
        y=approx.ravel()[1]
        if len(approx)==3:
            cv2.putText(img,'Triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        if len(approx)==4:
            x1,y1,w,h=cv2.boundingRect(approx)
            aspect_ratio=w/h
            if aspect_ratio>0.98 and aspect_ratio<1.2:
                cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            else:
                dist=[]
                for i in range(2):
                    dist.append(np.sum((approx[i][0]-approx[i+2][0])**2))
                if 0<=abs(dist[0]-dist[1])<=200:
                    cv2.putText(img, 'Rectangle', (x, y),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                else:
                    cv2.putText(img, 'Parallelogram', (x, y),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        if 15>len(approx)>6:
            cv2.putText(img,'Elipse',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        if len(approx)>=15:
            cv2.putText(img,'Circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
cv2.imshow('shape', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
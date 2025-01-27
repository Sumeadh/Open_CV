import numpy as np
import cv2 as cv
'''
def click(event,x,y,flag,form):
    if event==cv.EVENT_LBUTTONDOWN:
        circle=cv.circle(img,(x,y),3,(255,255,0),-1)
        points.append((x,y))
        if len(points)>=2:
            line=cv.line(img,points[-2],points[-1],(0,255,255),1)
        cv.imshow('img1',img)

img=np.zeros((512,512,3),np.uint8)
print(type(img))
points=[]
cv.imshow('img1',img)
cv.setMouseCallback('img1',click)
cv.waitKey(0)
cv.destroyAllWindows()
'''

def click(event,x,y,flag,form):
    if event==cv.EVENT_LBUTTONDOWN:
        blue=img[y,x,0]# 0 based index in  image represents the y coordinates and 1 for x
        green = img[y, x, 1]
        red=img[y,x,2]
        colour=np.zeros((512,512,3),np.uint8)
        colour[:]=[blue,green,red]
        cv.imshow('coloured window',colour)
img=cv.imread('lena.jpg')
cv.imshow('img', img)
cv.setMouseCallback('img',click)
cv.waitKey(0)
cv.destroyAllWindows()
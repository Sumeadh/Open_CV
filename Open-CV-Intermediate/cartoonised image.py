import cv2
import numpy as np

# Load the image
img = cv2.imread('trump.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Edges
blurred_img=cv2.medianBlur(gray,1)
#edges=cv2.Canny(blurred_img,75,150)
edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,11)
cv2.imshow('Edge Image', edges)
#color
color=cv2.bilateralFilter(img,10,30,300)
#cartoon
#kernal=np.ones((1,1),np.uint8)
#dilation = cv2.dilate(edges , kernal,  iterations = 1)
#erosion=cv2.erode(dilation , kernal,  iterations = 1)
edges_new = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
cv2.imshow('new edge Image', edges_new)

cartoon=cv2.bitwise_and(color,edges_new)

# Display the original and cartoon images
cv2.imshow('Original Image', img)
cv2.imshow('Cartoon Image', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

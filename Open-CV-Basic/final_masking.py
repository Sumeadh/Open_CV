import cv2
import numpy as np

# read image
img = cv2.imread(r"C:\Users\Sumeadh\Desktop\PROGRAMS\OPEN CV\TULIP.jpg")

# Convert BGR to HSV (easier for color segmentation)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of yellow color in HSV
lower_yellow = np.array([0,90,150])
upper_yellow = np.array([255,255,255])

# Create a mask using the defined ranges    
mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)
#array of 0 and 255 
'''
for i in mask:
    print(i)
'''

# Bitwise-AND mask and original image
result = cv2.bitwise_and(img,img, mask= mask1)

cv2.imwrite('masked_tulip.jpg',result)
# display the masked image
cv2.imshow('Original',img)
cv2.imshow('Masked Image',result)
cv2.imshow('mask',mask1)
cv2.waitKey(0)
cv2.destroyAllWindows()

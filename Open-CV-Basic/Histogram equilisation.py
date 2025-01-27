import numpy as np
from matplotlib import pyplot as plt
import cv2

img=cv2.imread('lion.jpeg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('INPUT IMAGE',img)

b,g,r=cv2.split(img)
h,s,v=cv2.split(img2)

hist=cv2.calcHist([img],[0],None,[256],[0,256])
hist2=cv2.calcHist([v],[0],None,[256],[0,256])

clahe=cv2.createCLAHE(clipLimit=5)
final_v=clahe.apply(v)
#final_v=cv2.equalizeHist(v)
final_b=clahe.apply(b)
final_g=clahe.apply(g)
final_r=clahe.apply(r)

img=cv2.merge((final_b,final_g,final_r))
img2=cv2.merge((h,s,final_v))
img2=cv2.cvtColor(img2,cv2.COLOR_HSV2BGR)
plt.plot(hist)
plt.show()


#Output display

cv2.imshow('CLIPPED IMAGE USING BGR',img)
cv2.imshow('CLIPPED IMAGE USING HSV',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

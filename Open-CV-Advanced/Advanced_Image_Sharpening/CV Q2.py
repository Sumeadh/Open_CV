import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
#Reading and displaying the image
img=cv2.imread("news.jpeg")
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
'''
hist=cv2.calcHist([img_gray],[0],None,[256],[0,256])
final_img=cv2.equalizeHist(img_gray)

h,s,v=cv2.split(img_hsv)
clahe=cv2.createCLAHE(clipLimit=5)
final_v=clahe.apply(v)
img_hsv=cv2.merge((h,s,final_v))
img_clipped=cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('original image', img)
cv2.imshow('equalized image',final_img)
cv2.imshow('clipped image',img_clipped)
'''

#plotting
'''
plt.plot(hist)
plt.plot(final_img)
plt.show()
'''
#image preprocesing
gaussian_blur=cv2.GaussianBlur(img,(7,7),15)
sharpend=cv2.addWeighted(img,4.5,gaussian_blur,-3.5,5)
cv2.imshow('sharpend image',sharpend)

#Text extraction
text = pytesseract.image_to_string(sharpend)
print(text)

#Counting the characters
alphabets=0
numbers=0
speacial_char=0

for i in text:
    if i.isalpha():
        alphabets+=1
    elif i.isnumeric():
        numbers+=1
    else:
        speacial_char+=1
print('the number of alphabets in the scanned text',alphabets)
print('the number of numbers in the scanned text',numbers)
print('the number of speacial characters in the scanned text',speacial_char)
cv2.waitKey(0)
cv2.destroyAllWindows()


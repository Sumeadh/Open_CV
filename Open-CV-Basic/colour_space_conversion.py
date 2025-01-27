import cv2
import numpy as np

#read image
img = cv2.imread(r"C:\Users\Sumeadh\Desktop\PROGRAMS\OPEN CV\TULIP.jpg")

#colorspace conversions
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#display images
cv2.imshow("Original",img)
cv2.imshow("Grayscale",gray)
cv2.imshow("HSV",hsv)
cv2.imshow("RGB",rgb)

#press any key to exit(destroy all windows)
cv2.waitKey(5000)
cv2.destroyAllWindows()
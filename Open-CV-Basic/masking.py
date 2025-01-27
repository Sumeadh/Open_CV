import cv2 as cv
import numpy as np

# read image
cap=cv.VideoCapture(0) 
while True:
    r, frame = cap.read()
    # Convert BGR to HSV (easier for color segmentation)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of red color in HSV
    lower = np.array([160, 100, 100])
    upper = np.array([180, 250, 250])
    # Create a mask using the defined ranges
    mask1 = cv.inRange(hsv, lower, upper)
    # array of 0 and 25
    # Bitwise-AND mask and original image
    result = cv.bitwise_and(frame, frame, mask=mask1)
    # display the masked image
    cv.imshow('Original', frame)
    cv.imshow('Masked Image', result)
    cv.imshow('mask', mask1)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

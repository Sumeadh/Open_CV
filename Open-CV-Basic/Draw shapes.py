import cv2
import numpy as np

img=np.ones((888,846,3))
cv2.rectangle(img,(150,150) , (250,700), [0,0,255], -1)
cv2.rectangle(img,(550,150) , (650,700), [0,0,255], -1)
cv2.rectangle(img,(250,400) , (550,700), [140,0,0], -1)

vertices=np.array([[125, 150], [275, 150], [200, 25]])
vertices2=np.array([[525, 150], [675, 150], [600, 25]])
vertices=vertices.reshape((-1,1,2))
vertices2=vertices2.reshape((-1,1,2))

cv2.fillPoly(img, [vertices], (0,255,0))
cv2.fillPoly(img, [vertices2], (0,255,0))
cv2.imshow('Output image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

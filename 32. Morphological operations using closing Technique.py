import cv2
import numpy as np
img=cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv.webp")
kernel=np.ones((5,5),np.uint8)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow('original',img)
cv2.imshow('closing',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
img=cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv.webp",cv2.IMREAD_GRAYSCALE)
kernel=np.ones((5,5),np.uint8)
blackchat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow('original',img)
cv2.imshow('blackhat',blackchat)
cv2.waitKey(0)
cv2.detroyAllWindows()

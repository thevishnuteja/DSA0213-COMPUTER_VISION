import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path="C:/Users/leela/OneDrive/Desktop/CV/cv.jpg"
img=cv2.imread(path)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggray,(7,7),0)
imgcanny=cv2.Canny(imgblur,100,200)
cv2.imshow("Img Canny",imgcanny)
cv2.waitKey(0)

import cv2
img=cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(3,3),0)
soblex=cv2.Sobel(src=img_blur,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
cv2.imshow('soblex',soblex)
cv2.waitKey(0)

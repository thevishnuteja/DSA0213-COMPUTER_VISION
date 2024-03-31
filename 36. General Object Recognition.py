import cv2
import numpy as np
watch_cascade=cv2.CascadeClassifier("C:/Users/leela/OneDrive/Desktop/CV/watch_cascade.xml")
img=cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/watch1.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
watches=watch_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)
for(x,y,w,h)in watches:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('watches detected',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

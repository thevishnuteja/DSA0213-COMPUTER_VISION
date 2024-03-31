import cv2
img=cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv.webp")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier()
faces=face_cascade.detectMultiScale(gray,ScaleFactor=1.1,minNeighbours=5)
for(x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('faces detected',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

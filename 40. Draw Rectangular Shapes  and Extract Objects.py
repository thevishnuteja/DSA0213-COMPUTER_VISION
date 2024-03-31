import cv2
img=cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv.webp")
x,y=100,100
width,height=200,150
roi=img[y:y+height,x:x+width]
cv2.imshow('roi',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
img=cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv.jpg")
cv2.waitKey(0)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(3,3),0)
edges=cv2.Canny(image=img_blur,threshold1=100,threshold2=200)
cv2.imshow('Canny edge detection',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
path="C:/Users/leela/OneDrive/Desktop/CV/cv.jpg"
src=cv2.imread(path)
window_name='image'
image=cv2.rotate(src,cv2.ROTATE_180)
cv2.imshow(window_name,image)
cv2.waitKey(0)

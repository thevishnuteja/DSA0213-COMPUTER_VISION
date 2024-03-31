import cv2
import numpy as np
image = cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv.webp")
img2 = cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv2.jpg")
if image.shape != img2.shape:
    img2 = cv2.resize(img2, (image.shape[1], image.shape[0]))
cv2.imshow('Original Image', image)
imagecopy = image.copy()
cv2.circle(imagecopy, (100, 100), 30, (255, 0, 0), -1)
cv2.imshow('Image with Circle', imagecopy)
cropped_image = image[80:280, 150:330]
cv2.imshow('Cropped Image', cropped_image)
dst = cv2.addWeighted(image, 0.5, img2, 0.7, 0)
cv2.imshow('Blended Image', dst)
img_arr = np.hstack((image, img2))
cv2.imshow('Input Images', img_arr)
cv2.waitKey(0)
cv2.destroyAllWindows()

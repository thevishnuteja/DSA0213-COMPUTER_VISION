import cv2
import numpy as np

def sharpen_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (0, 0), 3)
    gradient = cv2.Laplacian(blurred, cv2.CV_64F)
    sharpened = cv2.addWeighted(gray.astype(np.float64), 1.5, gradient, -0.5, 0)
    sharpened_image = cv2.cvtColor(sharpened.astype(np.uint8), cv2.COLOR_GRAY2BGR)

    return sharpened_image
input_image = cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv.webp")
sharpened_result = sharpen_image(input_image)
cv2.imshow('Original Image', input_image)
cv2.imshow('Sharpened Image', sharpened_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

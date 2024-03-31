import cv2
import numpy as np

def high_boost_sharpening(image, alpha):
  if len(image.shape) == 3:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


  blur = cv2.GaussianBlur(image, (3, 3), 0)

  laplacian = cv2.Laplacian(blur, cv2.CV_64F)


  high_boost_mask = 1 + alpha * laplacian


  sharpened_image = image + high_boost_mask * (image - blur)
  sharpened_image = np.uint8(np.clip(sharpened_image, 0, 255))

  return sharpened_image


image = cv2.imread("C:/Users/leela/OneDrive/Desktop/CV/cv.webp")

sharpened_image = high_boost_sharpening(image.copy(), alpha=1.0)


cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

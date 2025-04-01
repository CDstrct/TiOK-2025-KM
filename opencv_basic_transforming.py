# import the necessary packages
import numpy as np
import cv2
# load the image and display it to our screen
image = cv2.imread("example.jpg")
cv2.imshow("Original", image)
# shift the image 25 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
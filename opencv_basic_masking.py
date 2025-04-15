import cv2
import numpy as np

image = cv2.imread("example.jpg")
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.ellipse(mask, (image.shape[1]//2, image.shape[0]//2), (250, 200), 0, 0, 360, 255, -1)
cv2.imshow(" Mask", mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

mask2 = np.zeros(image.shape[:2], dtype="uint8")
cv2.ellipse(mask2, (image.shape[1]//2, image.shape[0]//2), (200, 50), 0, 0, 360, 255, -1)
cv2.imshow("Rectangular Mask", mask2)
cv2.waitKey(0)

inverted_mask = cv2.bitwise_not(mask2)
masked2 = cv2.bitwise_and(image, image, mask=inverted_mask)

cv2.imshow("Mask Applied to Image", masked2)
cv2.waitKey(0)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

result = cv2.bitwise_and(image, image, mask=red_mask)

cv2.imshow("Maska czerwonego", red_mask)
cv2.waitKey(0)
cv2.imshow("Tylko czerwony kolor", result)
cv2.waitKey(0)

import numpy as np
import cv2
import imutils

image = cv2.imread("example.jpg")
cv2.imshow("Original", image)

M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted1", shifted1)

M = np.float32([[1, 0, -20], [0, 1, -50]])
shifted2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("shifted2", shifted2)
cv2.waitKey(0)


shifted3 = imutils.translate(image, 100, 50)
cv2.imshow("Shifted3", shifted3)
cv2.waitKey(0)

X = int(input("Podaj przesunięcie X: "))
Y = int(input("Podaj przesunięcie Y: "))
shifted4 = imutils.translate(image, X, Y)
cv2.imshow("Shifted4", shifted4)
cv2.waitKey(0)
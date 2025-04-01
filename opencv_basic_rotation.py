
import cv2
import imutils
import argparse

image = cv2.imread("example2.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey()

M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey()

M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Arbitrary Point", rotated)
cv2.waitKey()


X = int(input("Podaj kąt obrotu: "))
rotated = imutils.rotate(image, X)
cv2.imshow("Rotated", rotated)
cv2.waitKey()

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey()

rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(0)
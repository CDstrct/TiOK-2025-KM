import numpy as np
import cv2

rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey()

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey()

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

triangle = np.zeros((300, 300, 3), dtype=np.uint8)

pts = np.array([[0, 250], [250, 250], [250, 0]], np.int32)

pts = pts.reshape((-1, 1, 2))

cv2.fillPoly(triangle, [pts], (255, 255, 255))
cv2.imshow("triangle",triangle)
cv2.waitKey()

bitwiseAnd = cv2.bitwise_and(triangle[:, :, 0], circle)
cv2.imshow("AND Triangle and Circle", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(triangle[:, :, 0], circle)
cv2.imshow("OR Triangle and Circle", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(triangle[:, :, 0], circle)
cv2.imshow("XOR Triangle and Circle", bitwiseXor)
cv2.waitKey(0)


bitwiseNot = cv2.bitwise_not(triangle[:, :, 0])
cv2.imshow("NOT Triangle", bitwiseNot)
cv2.waitKey(0)




image = cv2.imread("example.jpg")
cv2.imshow("image",image)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey()

bitwiseAnd = cv2.bitwise_and(image, flipped)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(image, flipped)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(image, flipped)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)
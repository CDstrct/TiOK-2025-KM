import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

blue = (255, 0, 0)
cv2.line(canvas, (300, 0), (0, 300), blue, 2)
cv2.imshow("Canvas1", canvas)
cv2.waitKey(0)

canvas2 = np.zeros((400, 400, 3), dtype="uint8")

green = (0, 255, 0)
cv2.rectangle(canvas2, (0, 0), (100, 40), green)
red = (0, 0, 255)
cv2.rectangle(canvas2, (350, 350), (400, 400), red)
cv2.imshow("Canvas2", canvas2)
cv2.waitKey(0)

canvas3 = np.zeros((300, 300, 3), dtype="uint8")

cv2.circle(canvas3, (40, 40), 40, (255, 0, 0), -1)
cv2.circle(canvas3, (150, 150), 60, (0, 0, 255), -1)

cv2.imshow("Canvas3", canvas3)
cv2.waitKey(0)


canvas4 = np.zeros((300, 300, 3), dtype="uint8")

cv2.rectangle(canvas4, (100, 100), (200, 200), (0, 255, 0), 2)
cv2.circle(canvas4, (150, 150), 30, (255, 255, 0), 2)

cv2.imshow("Canvas4", canvas4)
cv2.waitKey(0)

canvas5 = np.zeros((400, 400, 3), dtype="uint8")
center = (200, 200)

for i in range(5):
    size = 40 + i * 20
    top_left = (center[0] - size//2, center[1] - size//2)
    bottom_right = (center[0] + size//2, center[1] + size//2)
    cv2.rectangle(canvas5, top_left, bottom_right, (0, 255, 255), 2)

cv2.imshow("Canvas5", canvas5)
cv2.waitKey(0)

canvas6 = cv2.imread("ex1.jpg")
cv2.circle(canvas6,(300, 370), 30, red, -1)
cv2.circle(canvas6,(460, 330), 30, red, -1)
cv2.rectangle(canvas6, (350, 500 ), (500, 600), green, -1)
cv2.circle(canvas6,(380, 400), 300, blue, 1)
cv2.imshow("Canvas6", canvas6)
cv2.waitKey(0)


import numpy as np
import cv2



image = cv2.imread("example.jpg")
cv2.imshow("image",image)
cv2.waitKey()


roi  = image[0:100, 0:100]
cv2.imshow("roi",roi    )
cv2.waitKey()

roi2 = image[337:, :]
cv2.imshow("roi2",roi2)
cv2.waitKey()

roi3 = image[:, 640:]
cv2.imshow("roi3",roi3)
cv2.waitKey()

startY = int(input("Podaj startY: "))
endY = int(input("Podaj endY: "))
startX = int(input("Podaj startX: "))
endX = int(input("Podaj endX: "))

roi4 = image[startY:endY, startX:endX]
cv2.imshow("roi4",roi4)
cv2.waitKey()

roi5  = image[100:500, 300:900]
cv2.imshow("roi5",roi5)
cv2.waitKey()

roi6 = image
roi6[200:300, 250:350] = roi
cv2.imshow("roi6",roi6)
cv2.waitKey()

roi9 = image[100:400, 100:400]


cv2.imshow("roi9", roi9)
cv2.waitKey(0)
cv2.imwrite("roi9.jpg", roi9)
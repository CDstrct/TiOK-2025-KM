import cv2
import numpy as np



image = cv2.imread("example.jpg")

bright_opencv = cv2.add(image, np.ones(image.shape, dtype=np.uint8) * 50)
cv2.imshow("cv", bright_opencv)
cv2.waitKey()

bright_numpy = image.astype(np.int16) + 50
bright_numpy = np.clip(bright_numpy, 0, 255).astype(np.uint8)
cv2.imshow("np", bright_numpy)
cv2.waitKey()

burn_numpy = image.astype(np.int16) + 150
burn_numpy = np.clip(burn_numpy, 0, 255).astype(np.uint8)
cv2.imshow("np", burn_numpy)
cv2.waitKey()

burn_opencv = cv2.add(image, np.ones(image.shape, dtype=np.uint8) * 150)
cv2.imshow("cv", burn_opencv)
cv2.waitKey()

dark_numpy = image.astype(np.int16) + -80
dark_numpy = np.clip(dark_numpy, 0, 255).astype(np.uint8)
cv2.imshow("np", dark_numpy)
cv2.waitKey()

dark_opencv = cv2.subtract(image, np.ones(image.shape, dtype=np.uint8) * 80)
cv2.imshow("cv", dark_opencv)
cv2.waitKey()

colors= np.clip(image.astype(np.int16) + [10, -20, 30], 0, 255).astype(np.uint8)
cv2.imshow("colors", colors)
cv2.waitKey()

M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

difference = cv2.absdiff(image, shifted1)
cv2.imshow("Różnica między obrazami", difference)
cv2.waitKey(0)
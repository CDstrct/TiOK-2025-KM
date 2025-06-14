import cv2

image = cv2.imread("example.jpg")
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.imwrite("RED.jpg", R)
cv2.imwrite("BLUE.jpg", B)
cv2.imwrite("GREEN.jpg", G)

cv2.waitKey(0)

B[:] = 0
merged = cv2.merge([G, B, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)

#DOKOŃCZ 4
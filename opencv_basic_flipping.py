import cv2

image = cv2.imread("example.jpg")
cv2.imshow("Original", image)
cv2.waitKey()

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey()

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey()

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)

(h, w) = image.shape[:2]
right_half = image[:, w//2:]

flipped_half = cv2.flip(right_half, 1)

image2 = cv2.imread("example.jpg")
image2[:, w//2:] = flipped_half

cv2.imshow("Odbicie prawej połowy", image2)
cv2.waitKey(0)

print("Wybierz sposób odbicia:")
print("0 - pionowe | 1 - poziome | -1 - oba")
choice = int(input("Twój wybór: "))

if choice not in [-1, 0, 1]:
    print("Nieprawidłowy wybór!")
else:
    flipped2 = cv2.flip(image, choice)
    cv2.imshow("Odbity obraz", flipped2)
    cv2.waitKey(0)

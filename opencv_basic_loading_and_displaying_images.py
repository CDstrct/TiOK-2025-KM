import cv2
# Wczytanie obrazu z pliku
image = cv2.imread("example.jpg")
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
  print("Błąd: nie można wczytać obrazu!")
else:
  print("Obraz wczytano poprawnie.")

# Wczytanie obrazu z pliku
image = cv2.imread("example.jpg")
(h, w, c) = image.shape[:3]
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')

image2 = cv2.imread("example2.jpg")
(h2, w2, c2) = image2.shape[:3]
print(f'width: {w2} pixels')
print(f'height: {h2} pixels')
print(f'channels: {c2}')

cv2.namedWindow("Obraz 1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Obraz 2", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Obraz 1", image.shape[1], image.shape[0])
cv2.resizeWindow("Obraz 2", image2.shape[1], image2.shape[0])

cv2.imshow("Obraz 1", image)
cv2.imshow("Obraz 2", image2)

cv2.waitKey(0)
cv2.destroyWindow("Obraz 1")

cv2.waitKey(0)
cv2.destroyWindow("Obraz 2")

image_gray = cv2.imread("example.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



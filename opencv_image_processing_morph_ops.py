import cv2

img = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

# 1.
erosion_sq = cv2.erode(binary, kernel_square, iterations=1)
erosion_el = cv2.erode(binary, kernel_ellipse, iterations=1)
cv2.imshow("1. Erozja - Kwadrat", erosion_sq)
cv2.waitKey()
cv2.imshow("1. Erozja - Elipsa", erosion_el)
cv2.waitKey()

# 2.
dil_3 = cv2.dilate(binary, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
dil_5 = cv2.dilate(binary, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
dil_7 = cv2.dilate(binary, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))
cv2.imshow("2. Dylatacja 3x3", dil_3)
cv2.waitKey()
cv2.imshow("2. Dylatacja 5x5", dil_5)
cv2.waitKey()
cv2.imshow("2. Dylatacja 7x7", dil_7)
cv2.waitKey()
# 3.
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel_square)
cv2.imshow("3. Otwarcie", opened)
cv2.waitKey()

# 4.
closed_rect = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_square)
closed_ellipse = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_ellipse)
cv2.imshow("4. Zamknięcie - prostokąt", closed_rect)
cv2.waitKey()
cv2.imshow("4. Zamknięcie - elipsa", closed_ellipse)
cv2.waitKey()
# 5.
for name, kernel in [("kwadrat", kernel_square), ("elipsa", kernel_ellipse), ("krzyż", kernel_cross)]:
    erosion = cv2.erode(binary, kernel)
    dilation = cv2.dilate(binary, kernel)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow(f"5. {name} - Erozja", erosion)
    cv2.waitKey()
    cv2.imshow(f"5. {name} - Dylatacja", dilation)
    cv2.waitKey()
    cv2.imshow(f"5. {name} - Otwarcie", opening)
    cv2.waitKey()
    cv2.imshow(f"5. {name} - Zamknięcie", closing)
    cv2.waitKey()
    cv2.imshow(f"5. {name} - Gradient", gradient)
    cv2.waitKey()
# 6.
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel_square)
improved = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel_square)
cv2.imshow("6. Poprawa obrazu", improved)
cv2.waitKey()

cv2.imshow("Oryginalny", binary)

cv2.waitKey(0)



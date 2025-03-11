import cv2

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Original", image)
cv2.waitKey(0)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# access the pixel located at x=50, y=20
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# update the pixel at (50, 20) and set it to red
image[0,859] = (0, 0, 255)
(b, g, r) = image[0, 859]
print("Pixel- Red: {}, Green: {}, Blue: {}".format( r, g, b))

cv2.imshow("Changed", image)
cv2.waitKey(0)

# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)

tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Left Corner", tl)
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)
cv2.waitKey(0)

#
image[0:cY, 0:cX] = (255, 0, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)

a = int(input(f"Podaj współrzędną x (0-{w-1}): "))
b = int(input(f"Podaj współrzędną y (0-{h-1}): "))

if 0 <= a < w and 0 <= b < h:
    image[b, a] = (0, 0, 0)
    (b, g, r) = image[a, b]
    cv2.imshow("black pixel", image)
    cv2.waitKey(0)
else:
    print("Błąd: Współrzędne poza zakresem obrazu.")

center_x, center_y = w// 2, h // 2

half_size = 50
x1, y1 = center_x - half_size, center_y - half_size
x2, y2 = center_x + half_size, center_y + half_size

image[y1:y2, x1:x2] = (0, 0, 255)

cv2.imshow("Modified Image", image)
cv2.waitKey(0)

(tX, tY) = (w // 3, h // 3)
m =image[tY:2*tY,tX:tX*2]
cv2.imshow("a",m)
cv2.waitKey(0)
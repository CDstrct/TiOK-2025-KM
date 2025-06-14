import cv2
import numpy as np

image = cv2.imread("example.jpg")
cv2.imshow("Original", image)
cv2.waitKey()
blur_avg = cv2.blur(image, (5, 5))
cv2.imshow("Average Blur", blur_avg)
cv2.waitKey()
blur_gauss = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Gaussian Blur", blur_gauss)
cv2.waitKey()
blur_median = cv2.medianBlur(image, 5)
cv2.imshow("Median Blur", blur_median)
cv2.waitKey()
blur_bilateral = cv2.bilateralFilter(image, 11, 41, 21)
cv2.imshow("Bilateral Blur", blur_bilateral)
cv2.waitKey()
cv2.destroyAllWindows()
kernel_sizes = [3, 5, 9, 15]

for size in kernel_sizes:
    cv2.imshow(f"Average {size}", cv2.blur(image, (size, size)))
    cv2.waitKey()
    cv2.imshow(f"Gaussian {size}", cv2.GaussianBlur(image, (size, size), 0))
    cv2.waitKey()
    cv2.imshow(f"Median {size}", cv2.medianBlur(image, size))
    cv2.waitKey()

cv2.destroyAllWindows()

params = [(9, 75, 75), (11, 150, 150), (15, 250, 250)]

for d, sc, ss in params:
    blurred = cv2.bilateralFilter(image, d, sc, ss)
    cv2.imshow(f"Bilateral d={d}, sc={sc}, ss={ss}", blurred)
    cv2.waitKey()

cv2.destroyAllWindows()

tekst_img = cv2.imread("tekst_image.jpg ")

for k in [3, 5, 9]:
    cv2.imshow(f"Text Average {k}", cv2.blur(tekst_img, (k, k)))
    cv2.imshow(f"Text Gaussian {k}", cv2.GaussianBlur(tekst_img, (k, k), 0))
    cv2.imshow(f"Text Median {k}", cv2.medianBlur(tekst_img, k))
    cv2.imshow(f"Text Bilateral {k}", cv2.bilateralFilter(tekst_img, k, 75, 75))
    cv2.waitKey()

cv2.destroyAllWindows()

noisy_image = image.copy()
noise = np.zeros_like(noisy_image)
cv2.randn(noise, 0, 50)
noisy_image = cv2.add(noisy_image, noise)

cv2.imshow("Noisy Image", noisy_image)
cv2.waitKey(0)

blur1 = cv2.blur(noisy_image, (5, 5))
blur2 = cv2.GaussianBlur(noisy_image, (5, 5), 0)
blur3 = cv2.medianBlur(noisy_image, 5)
blur4 = cv2.bilateralFilter(noisy_image, 11, 75, 75)

cv2.imshow("Average", blur1)
cv2.waitKey()
cv2.imshow("Gaussian", blur2)
cv2.waitKey()
cv2.imshow("Median", blur3)
cv2.waitKey()
cv2.imshow("Bilateral", blur4)
cv2.waitKey()
cv2.destroyAllWindows()

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (100, 100), (300, 300), 255, -1)

blurred_background = cv2.GaussianBlur(image, (21, 21), 0)

final = np.where(mask[:, :, np.newaxis] == 255, image, blurred_background)

cv2.imshow("Depth of Field Simulation", final)
cv2.waitKey(0)
cv2.destroyAllWindows()


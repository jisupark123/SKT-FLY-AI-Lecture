import cv2
import numpy as np


def salt_pepper_noise(img, n):
    h, w = img.shape[:2]
    x, y = np.random.randint(0, w, n), np.random.randint(0, h, n)
    noise = img.copy()
    for x, y in zip(x, y):
        noise[y, x] = 0 if np.random.rand() < 0.5 else 255

    return noise


img = cv2.imread("week4/chap07/images/median2.jpg", cv2.IMREAD_GRAYSCALE)

noise = salt_pepper_noise(img, 500)
th_img = cv2.threshold(noise, 128, 255, cv2.THRESH_BINARY)[1]
data = [0, 1, 0, 1, 1, 1, 0, 1, 0]  # 마스크 선언 및 초기화
mask = np.array(data, np.uint8).reshape(3, 3)

erode_img = cv2.erode(th_img, mask)
dilate_img = cv2.dilate(th_img, mask)

cv2.imshow("img", img)
cv2.imshow("noise", noise)
cv2.imshow("th_img", th_img)
cv2.imshow("erode_img", erode_img)
cv2.imshow("dilate_img", dilate_img)
cv2.waitKey(0)

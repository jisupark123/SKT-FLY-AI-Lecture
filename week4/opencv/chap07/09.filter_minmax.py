import numpy as np, cv2


def minmax_filter(image, ksize, mode):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2

    for i in range(center, rows - center):
        for j in range(center, cols - center):
            y1, y2 = i - center, i + center + 1
            x1, x2 = j - center, j + center + 1

            roi = image[y1:y2, x1:x2]
            dst[i, j] = cv2.minMaxLoc(roi)[mode]  # 최소값 또는 최대값 반환

    return dst


image = cv2.imread("week4/chap07/images/min_max.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

minfilter_img = minmax_filter(image, 3, 0)
maxfilter_img = minmax_filter(image, 3, 1)

cv2.imshow("image", image)
cv2.imshow("minfilter_img", minfilter_img)
cv2.imshow("maxfilter_img", maxfilter_img)
cv2.waitKey(0)

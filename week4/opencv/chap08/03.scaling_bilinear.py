import numpy as np, cv2

image = cv2.imread("week4/Chap08/images/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 에러")


def upscaling(img, scale):
    h, w = img.shape[:2]
    dst = np.zeros((h * scale, w * scale), img.dtype)
    for i in range(h):
        for j in range(w):
            dst[i * scale : (i + 1) * scale, j * scale : (j + 1) * scale] = img[i, j]
    return dst


h, w = image.shape[:2]

size = (w * 4, h * 4)
dst1 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR)
dst2 = cv2.resize(image, size, 0, 0, cv2.INTER_NEAREST)
dst3 = upscaling(image, 4)


cv2.imshow("image", image)
cv2.imshow("OpenCV_linear", dst1)
cv2.imshow("OpenCV_Nearest", dst2)
cv2.imshow("User_Nearest", dst3)
cv2.waitKey(0)

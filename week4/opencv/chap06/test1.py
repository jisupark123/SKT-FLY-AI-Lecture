import numpy as np, cv2

image1 = cv2.imread("week4/chap06/images/add1.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
image2 = cv2.imread("week4/chap06/images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 영상 합성

alpha, beta = map(float, input("alpha, beta >> ").split())
img = cv2.addWeighted(image1, alpha, image2, beta, 0)  # 영상 합성


cv2.imshow(f"{alpha} {beta}", img)
cv2.waitKey(0)

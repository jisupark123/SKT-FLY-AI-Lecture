import numpy as np, cv2

image = cv2.imread("week4/chap07/images/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류")


canny2 = cv2.Canny(image, 50, 100)  # 캐니 에지 검출

cv2.imshow("image", image)
cv2.imshow("OpenCV_Canny", canny2)  # OpenCV 캐니 에지
cv2.waitKey(0)

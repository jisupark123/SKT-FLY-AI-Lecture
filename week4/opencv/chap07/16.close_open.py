import numpy as np, cv2
from Common.filters import erode, dilate


def opening(img, mask):  # 열림 연산
    tmp = erode(img, mask)  # 침식
    dst = dilate(tmp, mask)  # 팽창
    return dst


def closing(img, mask):  # 닫힘 연산
    tmp = dilate(img, mask)
    dst = erode(tmp, mask)
    return dst


image = cv2.imread("week4/chap07/images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

mask = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype("uint8")  # 마스크 초기화
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]  # 영상 이진화

# dst1 = opening(th_img, mask)  # 사용자 정의 열림 함수 호출
# dst2 = closing(th_img, mask)  # 사용자 정의 닫힘 함수 호출
dst3 = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)  # OpenCV의 열림 함수
dst4 = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=1)  # OpenCV의 닫힘 함수
open_fn = lambda x: cv2.morphologyEx(x, cv2.MORPH_OPEN, mask)
closing_fn = lambda x: cv2.morphologyEx(x, cv2.MORPH_CLOSE, mask, iterations=1)
dst5 = open_fn(open_fn(th_img))
dst6 = closing_fn(closing_fn(th_img))

# cv2.imshow("User opening", dst1)
# cv2.imshow("User closing", dst2)
cv2.imshow("OpenCV opening", dst3)
cv2.imshow("OpenCV closing", dst4)
cv2.imshow("OpenCV opening2", dst5)
cv2.imshow("OpenCV closing2", dst6)
cv2.waitKey(0)

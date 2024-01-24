import numpy as np, cv2

image = cv2.imread("week4/chap07/images/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류")


# 캐니 에지 트랙바 콜백 함수
# 두번째 인자 값만 바꿔줌
def trackbar1(pos):
    global thrs1
    thrs1 = pos
    edge = cv2.Canny(image, thrs1, thrs2)
    cv2.imshow("edge", edge)


def trackbar2(pos):
    global thrs2
    thrs2 = pos
    edge = cv2.Canny(image, thrs1, thrs2)
    cv2.imshow("edge", edge)


thrs1 = 50
thrs2 = 100
canny2 = cv2.Canny(image, 50, 100)  # 캐니 에지 검출

cv2.imshow("image", image)
cv2.namedWindow("edge", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("threshold1", "edge", thrs1, 255, trackbar1)
cv2.createTrackbar("threshold2", "edge", thrs2, 255, trackbar2)
cv2.imshow("edge", canny2)
cv2.waitKey(0)

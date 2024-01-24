import cv2

"""
cv2.THRESH_BINARY - 조건을 만족하는 픽셀값을 255로 만족하지 않는 픽셀값을 0으로 설정
cv2.THRESH_BINARY_INV - 조건을 만족하는 픽셀값을 0로 만족하지 않는 픽셀값을 255으로 설정
cv2.THRESH_TRUNC - 조건을 만족하는 픽셀값을 255로 만족하지 않는 픽셀값을 원본값으로 설정
cv2.THRESH_TOZERO - 조건을 만족하는 픽셀값을 원본값으로 만족하지 않는 픽셀값을 0으로 설정 
cv2.THRESH_TOZERO_INV - 조건을 만족하는 픽셀값을 0로 만족하지 않는 픽셀값을 원본값으로 설정
"""


def onThreshold(value, thresh_type, name):
    result = cv2.threshold(image, value, 255, thresh_type)[1]
    cv2.imshow(name, result)


image = cv2.imread("week4/chap06/images/color_space.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 오류")

cv2.namedWindow("result")
cv2.createTrackbar("threshold", "result", 128, 255, onThreshold)  # 트랙바 생성

thresh_types = [
    ("BINARY", cv2.THRESH_BINARY),
    ("BINARY_INV", cv2.THRESH_BINARY_INV),
    ("TRUNC", cv2.THRESH_TRUNC),
    ("TOZERO", cv2.THRESH_TOZERO),
    ("TOZERO_INV", cv2.THRESH_TOZERO_INV),
]
for name, t in thresh_types:
    # 한번에 모든 트랙바를 생성하고 싶다면 아래와 같이 반복문을 사용하면 된다.
    onThreshold(128, t, name)

cv2.imshow("image", image)
cv2.waitKey(0)

"""
openCV와 numpy의 화소값 처리 방식 비교

openCV: 0~255 범위를 벗어나는 화소값은 0 또는 255로 고정
numpy: 0~255 범위를 벗어나는 화소값은 256으로 나눈 나머지 값으로 처리
"""
import cv2


image = cv2.imread("week4/chap06/images/bright.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None:
    raise Exception("영상 파일 읽기 오류")

dst1 = cv2.add(image, 100)  # 밝게
dst2 = cv2.subtract(image, 100)  # 어둡게

dst3 = image + 100  # 밝게 (numpy)
dst4 = image - 100  # 어둡게 (numpy)

# OpenCV 함수 이용
cv2.imshow("original image", image)
cv2.imshow("dst1- bright: OpenCV", dst1)
cv2.imshow("dst2- dark: OpenCV", dst2)
cv2.imshow("dst3- bright: numpy", dst3)
cv2.imshow("dst4- dark: numpy", dst4)
cv2.waitKey(0)

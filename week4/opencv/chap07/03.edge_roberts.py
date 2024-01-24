import numpy as np, cv2
from Common.filters import filter


def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)  # 입력 인자로 마스크 행렬 초기화
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter(image, mask1)
    dst2 = filter(image, mask2)
    dst1, dst2 = np.abs(dst1), np.abs(dst2)  # 컨볼류션 결과 행렬 양수 변경
    dst = cv2.magnitude(dst1, dst2)  # 컨볼류션 결과 두 행렬의 크기 계산

    return dst, dst1, dst2


image = cv2.imread("week4/chap07/images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 0, 0, 1, 0, 0, 0, 0]
data2 = [0, 0, -1, 0, 1, 0, 0, 0, 0]
dst, dst1, dst2 = differential(image, data1, data2)  # 컨볼류션 수행 및 두 방향의 크기 계산

cv2.imshow("image", image)
cv2.imshow("roberts edge", dst)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)

import numpy as np, cv2

image_path = "week4/chap05/images/minMax.jpg"

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")


min_val, max_val, _, _ = cv2.minMaxLoc(image)  # 최솟값, 최댓값 찾기

ratio = 255 / (max_val - min_val)  # 비율 계산
dst = np.round((image - min_val) * ratio).astype("uint8")  # 영상 확장
min_dst, max_dst, _, _ = cv2.minMaxLoc(dst)  # 최솟값, 최댓값 찾기


print("원본 영상 최솟값= %d , 최댓값= %d" % (min_val, max_val))
print("수정 영상 최솟값= %d , 최댓값= %d" % (min_dst, max_dst))
cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey(0)

import numpy as np, cv2

image = cv2.imread("week4/Chap08/images/affine.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일을 읽기 에러")

center = (image.shape[1] / 2, image.shape[0] / 2)  # 회전 중심
angle, scale = 30, 1
size = image.shape[::-1]  # 역순으로 정렬

pt1 = np.array([[30, 70], [20, 240], [300, 110]], np.float32)  # 변환 전 3개 좌표
pt2 = np.array([[120, 20], [10, 180], [280, 260]], np.float32)  # 변환 후 3개 좌표

aff_mat = cv2.getAffineTransform(pt1, pt2)  # 3개 좌표로 변환 행렬 계산
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)  # 회전 변환 행렬 계산

dst1 = cv2.warpAffine(image, aff_mat, size, cv2.INTER_LINEAR)  # 어파인 변환
dst2 = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)  # 회전 변환

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
dst1 = cv2.cvtColor(dst1, cv2.COLOR_GRAY2BGR)

for i in range(len(pt1)):
    cv2.circle(image, tuple(pt1[i].astype(int)), 3, (0, 0, 255), 2)
    cv2.circle(dst1, tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)

cv2.imshow("image", image)
cv2.imshow("dst1_OpenCV_affine", dst1)
cv2.imshow("dst4_OpenCV_affine_rotate", dst2)
cv2.waitKey(0)

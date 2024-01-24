import numpy as np, cv2

image = cv2.imread("week4/Chap08/images/perspective.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일을 읽기 에러")


pts1 = np.float32([(80, 40), (315, 133), (75, 300), (335, 300)])  # 입력 영상 좌표
pts2 = np.float32([(50, 60), (340, 60), (50, 320), (340, 320)])  # 출력 영상 좌표

perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)  # 투시 변환 행렬 계산
dst = cv2.warpPerspective(image, perspect_mat, (350, 400))  # 투시 변환 적용

cv2.imshow("image", image)
cv2.imshow("dst_perspective", dst)
cv2.waitKey(0)

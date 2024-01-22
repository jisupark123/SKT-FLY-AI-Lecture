import cv2

image_path = "/Users/my_home/Documents/Python/skt_fly_ai/week4/chap04/images/"

image = cv2.imread(
    image_path + "read_color.jpg",
    cv2.IMREAD_COLOR,
)
if image is None:
    raise Exception("영상 파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)  # JPG 화질 설정
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]  # PNG 압축 레벨 설정

## 행렬을 영상 파일로 저장
cv2.imwrite(image_path + "write_test1.jpg", image)  # 디폴트 설정
cv2.imwrite(image_path + "write_test2.jpg", image, params_jpg)  # JPG 파일로 저장
cv2.imwrite(image_path + "write_test3.png", image, params_png)  # PNG 파일로 저장
cv2.imwrite(image_path + "write_test4.bmp", image)  # BMP 파일로 저장
print("저장 완료")

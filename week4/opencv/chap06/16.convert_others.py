import cv2

BGR_img = cv2.imread("week4/chap06/images/color_space.jpg", cv2.IMREAD_COLOR)
if BGR_img is None:
    raise Exception("영상 파일 읽기 오류")

Gray_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2GRAY)  # BGR -> Gray
YCC_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2YCrCb)  # BGR -> YCC
YUV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2YUV)  # BGR -> YUV
Lab_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2LAB)  # BGR -> Lab

YCC_ch = cv2.split(YCC_img)  # YCC 채널 분리
YUV_ch = cv2.split(YUV_img)  # YUV 채널 분리
Lab_ch = cv2.split(Lab_img)  # Lab 채널 분리

cv2.imshow("BGR_img", BGR_img)
cv2.imshow("Gray_img", Gray_img)

sp1, sp2, sp3 = ["Y", "Cr", "Cb"], ["Y", "U", "V"], ["L", "A", "B"]
for i in range(len(sp1)):
    cv2.imshow(f"YCC_img[{i}]-{sp1[i]}", YCC_ch[i])
    cv2.imshow(f"YUV_img[{i}]-{sp2[i]}", YUV_ch[i])
    cv2.imshow(f"Lab_img[{i}]-{sp3[i]}", Lab_ch[i])
cv2.waitKey(0)

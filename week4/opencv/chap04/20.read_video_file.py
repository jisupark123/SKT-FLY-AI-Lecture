import cv2
from Common.utils import put_string

image_path = "/Users/my_home/Documents/Python/skt_fly_ai/week4/chap04/images/"

capture = cv2.VideoCapture(image_path + "move_file.avi")  # 동영상 파일 개방
if not capture.isOpened():
    raise Exception("동영상 파일 개방 안됨")  # 예외 처리

frame_rate = capture.get(cv2.CAP_PROP_FPS)  # 초당 프레임 수
delay = int(1000 / frame_rate)  # 지연 시간
frame_cnt = 0  # 현재 프레임 번호

while True:
    ret, frame = capture.read()  # 1개 프레임 읽기
    if not ret or cv2.waitKey(delay) >= 0:
        break
    blue, green, red = cv2.split(frame)  # 채널 분리
    frame_cnt += 1

    if frame_cnt % 3 == 0:
        cv2.add(blue, 100, blue)
    elif frame_cnt % 3 == 1:
        cv2.add(green, 100, green)
    elif frame_cnt % 3 == 2:
        cv2.add(red, 100, red)

    frame = cv2.merge([blue, green, red])  # 단일채널 영상 합성
    put_string(frame, "frame_cnt : ", (20, 320), frame_cnt)
    cv2.imshow("Read Video File", frame)

capture.release()

import cv2 as cv
import mediapipe as mp

capture = cv.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

mp_face_detection = mp.solutions.face_detection  # 얼굴 검출 모듈 생성
mp_drawing = mp.solutions.drawing_utils  # 그리기 모듈 생성

# 모델 선택
face_detection = mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5
)

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret:
        break
    if cv.waitKey(30) >= 0:
        break

    exposure = capture.get(cv.CAP_PROP_EXPOSURE)  # 노출값 획득
    result = face_detection.process(cv.cvtColor(frame, cv.COLOR_BGR2RGB))  # 얼굴 검출 수행
    frame = cv.blur(frame, (50, 50))
    for detection in result.detections:
        mp_drawing.draw_detection(frame, detection)  # 검출 결과 화면 출력

    title = "View Frame from Camera"
    # blur 처리
    cv.imshow(title, frame)  # 윈도우에 영상 띄우기
capture.release()

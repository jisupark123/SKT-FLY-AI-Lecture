import cv2 as cv
import mediapipe as mp

img = cv.imread("week4/chap08/images/face_image6.jpeg")
img_copy = img.copy()

mp_face_detection = mp.solutions.face_detection  # 얼굴 검출 모듈 생성
mp_drawing = mp.solutions.drawing_utils  # 그리기 모듈 생성

face_detection = mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5
)  # 모델 선택

result = face_detection.process(cv.cvtColor(img_copy, cv.COLOR_BGR2RGB))  # 얼굴 검출 수행

if not result.detections:
    raise Exception("얼굴 검출 실패")

for detection in result.detections:
    mp_drawing.draw_detection(img_copy, detection)  # 검출 결과 화면 출력

cv.imshow("image", img)
cv.imshow("result", img_copy)
cv.waitKey(0)
cv.destroyAllWindows()

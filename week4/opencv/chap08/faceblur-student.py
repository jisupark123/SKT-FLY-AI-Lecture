import cv2
import numpy as np

xml = "week4/chap08/images/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(xml)

cap = cv2.VideoCapture(0)  # 노트북 웹캠을 카메라로 사용
cap.set(3, 640)  # 너비
cap.set(4, 480)  # 높이


def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)  # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1] // 2, mask.shape[0] // 2  # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1  # 관심영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1  # 관심영역 너비 범위

            roi = image[y1:y2, x1:x2].astype("float32")  # 관심영역 형변환
            tmp = cv2.multiply(roi, mask)  # 회선 적용
            dst[i, j] = cv2.sumElems(tmp)[0]  # 출력화소 저장

    return dst  # 자료형 변환하여 반환


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # 좌우 대칭
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.05, 5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 얼굴에 사각형 표시
        face_img = frame[y : y + h, x : x + w]  # 탐지된 얼굴 이미지 crop
        # face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04)  # 축소
        # face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_NEAREST)  # 확대
        mask = (np.array([1 / 9]) * 9).reshape(3, 3)
        face_img = filter(face_img, mask)  # 회선 수행
        frame[y : y + h, x : x + w] = face_img  # 탐지된 얼굴 영역 모자이크 처리

    cv2.imshow("result", frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # Esc 키를 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()

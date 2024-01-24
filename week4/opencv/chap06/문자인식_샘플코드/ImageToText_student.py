import cv2
import numpy as np
import pytesseract as pt

TESSERACT_PATH = "C:/Program Files/Tesseract-OCR/tesseract.exe"  # 테서렉스 설치 경로
imgpath = "week4/chap06/문자인식_샘플코드/images/1.jpg"  # 이미지 파일 경로
win_name = "Image To Text"  # OpenCV 창 이름
img = cv2.imread(imgpath)  # 이미지 읽어오기
draw = img.copy()  # 출력용 이미지 별도 보관
pts_cnt = 0  # 마우스 클릭 수
pts = np.zeros((4, 2), dtype=np.float32)  # 마우스 클릭 좌표 저장용


# 마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global pts_cnt, img
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)

        pts[pts_cnt] = [x, y]
        pts_cnt += 1

        if pts_cnt == 4:
            sm = pts.sum(axis=1)  # 4개 좌표 각각 x+y 합
            diff = np.diff(pts, axis=1)  # 4개 좌표 각각 x-y 차
            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]

            # 변환 전 4개 좌표
            pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

            # 변환 후 영상에 사용할 서류의 폭과 높이 계산
            w1 = abs(bottomRight[0] - bottomLeft[0])
            w2 = abs(topRight[0] - topLeft[0])
            h1 = abs(topRight[1] - bottomRight[1])
            h2 = abs(topLeft[1] - bottomLeft[1])
            width = int(max([w1, w2]))
            height = int(max([h1, h2]))

            # 변환 후 4개 좌표
            pts2 = np.float32(
                [[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]]
            )

            # 변환 행렬 계산
            mtrx = cv2.getPerspectiveTransform(pts1, pts2)

            # 원근 변환 적용
            result = cv2.warpPerspective(img, mtrx, (width, height))
            cv2.imshow("scanned", result)
            img = result.copy()


# 이미치 처리 함수
def ImgProcessing():
    global img

    # 이미지 그레이 스케일 변환
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 이미지 음영 평준화
    norm_img = np.zeros(img.shape)
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)

    # 이미지 블러링
    img = cv2.GaussianBlur(img, (3, 3), 0)

    # 이미지 이산화
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 처리된 이미지 출력
    cv2.imshow("Image Processing", img)


# OCR 함수
def GetOCR():
    # OCR모델로 글자 추출
    text = pt.image_to_string(img, lang="kor+eng")

    return text


cv2.imshow(win_name, img)  # 이미지 출력
cv2.setMouseCallback(win_name, onMouse)  # 마우스 이벤트 등록
cv2.waitKey(0)
ImgProcessing()  # 이미지 처리
cv2.waitKey(0)
text: str = GetOCR()  # OCR함수로 텍스트 추출
print(text.replace("\n", " "))  # 텍스트 출력

import cv2
import numpy as np


def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x - 15, y - 15), (x + 15, y + 15), (0, 0, 255))
        cv2.imshow(title, image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), 10, (0, 0, 0))
        cv2.imshow(title, image)


image = np.full((200, 300), 255, np.uint8)
title = "Mouse Event"
cv2.imshow(title, image)  # 영상 보기

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from collections import deque

n, m = 480, 680

colors = {
    "red": (0, 0, 255),
    "green": (0, 255, 0),
    "blue": (255, 0, 0),
}

colors_reverse = {
    (0, 0, 255): "red",
    (0, 255, 0): "green",
    (255, 0, 0): "blue",
}


def draw_text(y, x, text, color):
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, color)


def draw_circle():
    cv2.circle(image, (100, 100), 50, colors["blue"], -1)
    cv2.circle(image, (400, 200), 60, colors["green"], -1)
    cv2.circle(image, (180, 300), 60, colors["red"], -1)
    cv2.circle(image, (300, 300), 40, colors["blue"], -1)
    cv2.circle(image, (500, 100), 20, colors["red"], -1)

    cv2.imshow(title, image)


# 상자 그리기
def draw_rect():
    # bfs로 원 판별
    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        min_x, min_y, max_x, max_y = j, i, j, i

        while queue:
            y, x = queue.popleft()
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            for a in range(4):
                ny, nx = y + dy[a], x + dx[a]

                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                    is_blank = np.all(image[ny][nx] == 255)
                    if not is_blank:
                        visited[ny][nx] = 1
                        # image[ny][nx] = (0, 0, 0)
                        # cv2.imshow(title, image)
                        queue.append((ny, nx))
        return (min_x, min_y), (max_x, max_y)

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            is_blank = np.all(image[i][j] == 255)

            if visited[i][j] == 0 and not is_blank:
                visited[i][j] = 1
                pt1, pt2 = bfs(i, j)
                color = image[i][j]
                color = (int(color[0]), int(color[1]), int(color[2]))

                cv2.rectangle(image, pt1, pt2, color, 1)
                # draw_text(pt1[1], pt1[0], colors_reverse[color], color)
                cv2.imshow(title, image)


image = np.full((n, m, 3), 255, np.uint8)

title = "Mouse Event"
cv2.imshow(title, image)  # 영상 보기

draw_circle()
draw_rect()
# print(np.all(image[400][120] == 255))

# cv2.waitKey(0)
cv2.destroyAllWindows()

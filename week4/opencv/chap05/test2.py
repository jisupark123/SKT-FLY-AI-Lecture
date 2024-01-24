visit = np.zeros_like(img)
q = []
q_idx = 0
result = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(3):
    for j in range(img.shape[0]):
        for k in range(img.shape[1]):
            if (
                np.sum(img[j, k, :]) == 255
                and np.sum(img[j, k, i]) == 255
                and visit[j, k, i] == 0
            ):
                q.append([j, k])
                xyxy = [img.shape[1], img.shape[0], 0, 0]

                while q_idx != len(q):
                    y = q[q_idx][0]
                    x = q[q_idx][1]
                    q_idx += 1
                    if visit[y, x, i] == 0:
                        visit[y, x, i] = 1
                        xyxy[0] = min(xyxy[0], x)
                        xyxy[1] = min(xyxy[1], y)
                        xyxy[2] = max(xyxy[2], x)
                        xyxy[3] = max(xyxy[3], y)

                        for l in range(4):
                            if (
                                img.shape[0] > y + dy[l] >= 0
                                and img.shape[1] > x + dx[l] >= 0
                            ):
                                if (
                                    np.sum(img[y + dy[l], x + dx[l], :]) == 255
                                    and np.sum(img[y + dy[l], x + dx[l], i]) == 255
                                    and visit[y + dy[l], x + dx[l], i] == 0
                                ):
                                    q.append([y + dy[l], x + dx[l]])
                result.append([xyxy, i])
                q.clear()
                q_idx = 0


color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_name = ["Blue", "Green", "Red"]
ret = img.copy()
for i in range(len(result)):
    ret = cv2.rectangle(
        ret, result[i][0][:2], result[i][0][2:], color[result[i][1]], 2, cv2.LINE_4
    )
    cv2.putText(
        ret,
        color_name[result[i][1]],
        (result[i][0][0] - 10, result[i][0][1] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
    )

plt.imshow(cv2.cvtColor(ret, cv2.COLOR_BGR2RGB))
plt.show()

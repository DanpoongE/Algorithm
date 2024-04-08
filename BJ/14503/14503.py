def next_way(x):
    if x - 1 < 0:
        return 3
    return x - 1

def is_messy(r, c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:     # 범위 내
            if arr[nr][nc] == 0:        # 청소 안 된 부분 있다면
                return 1

    return 0        # 청소했거나(2), 벽이라면(1) 0 출력


N, M = map(int, input().split())
robot_r, robot_c, way = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ans = 0
to_go = (robot_r, robot_c)

while to_go:
    now_r, now_c = to_go

    if arr[now_r][now_c] == 0:  # 청소되지 않은 칸이라면
        arr[now_r][now_c] = 2   # 청소하고
        ans += 1    # 청소한 칸 수 1개 늘리기

    else:   # 청소된 칸이고
        if is_messy(now_r, now_c):  # 주변에 아직 청소 안 된 칸이 있다면
            way = next_way(way)
            if way == 0:    # 북쪽
                if arr[now_r - 1][now_c] == 0:
                    to_go = (now_r - 1, now_c)
            elif way == 1:  # 동쪽
                if arr[now_r][now_c + 1] == 0:
                    to_go = (now_r, now_c + 1)
            elif way == 2:  # 남쪽
                if arr[now_r + 1][now_c] == 0:
                    to_go = (now_r + 1, now_c)
            elif way == 3:  # 서쪽
                if arr[now_r][now_c - 1] == 0:
                    to_go = (now_r, now_c - 1)

        else:   # 주변에 청소 안 된 칸이 없거나 다 벽이라면
            # 후진할 수 있으면 뒤로 후진
            if way == 0:    # 북쪽
                if arr[now_r + 1][now_c] != 1:
                    to_go = (now_r + 1, now_c)
                else:   # 벽(1)이라면 작동을 멈춘다.
                    break
            elif way == 1:  # 동쪽
                if arr[now_r][now_c - 1] != 1:
                    to_go = (now_r, now_c - 1)
                else:   # 벽(1)이라면
                    break
            elif way == 2:  # 남쪽
                if arr[now_r - 1][now_c] != 1:
                    to_go = (now_r - 1, now_c)
                else:   # 벽(1)이라면
                    break
            elif way == 3:  # 서쪽
                if arr[now_r][now_c + 1] != 1:
                    to_go = (now_r, now_c + 1)
                else:   # 벽(1)이라면
                    break

print(ans)
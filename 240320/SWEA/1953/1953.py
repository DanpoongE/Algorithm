from collections import deque
T = int(input())

left_lst = [[], [1, 3, 4, 5], [], [1, 3, 4, 5], [], [], [1, 3, 4, 5], [1, 3, 4, 5]]
right_lst = [[], [1, 3, 6, 7], [], [1, 3, 6, 7], [1, 3, 6, 7], [1, 3, 6, 7], [], []]
up_lst = [[], [1, 2, 5, 6], [1, 2, 5, 6], [], [1, 2, 5, 6], [], [], [1, 2, 5, 6]]
down_lst = [[], [1, 2, 4, 7], [1, 2, 4, 7], [], [], [1, 2, 4, 7], [1, 2, 4, 7], []]

for x in range(1, T + 1):
    N, M, R, C, L = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    moved = [[0] * M for _ in range(N)]
    runaway = deque()

    moved[R][C] = 1     # 첫 맨홀 기록
    runaway.append([R, C])
    cnt = 1

    while runaway:
        r, c = runaway.popleft()
        now = board[r][c]

        if moved[r][c] == L:
            break

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M: # 행렬 범위 내
                if k == 0:      # 오른쪽 탐색
                    if board[nr][nc] in right_lst[now] and moved[nr][nc] == 0:  # 갈 수 있는 길이고 간 적이 없다면
                        runaway.append([nr, nc])
                        moved[nr][nc] = moved[r][c] + 1
                        cnt += 1

                elif k == 1:    # 아래쪽 탐색
                    if board[nr][nc] in down_lst[now] and moved[nr][nc] == 0:  # 갈 수 있는 길이고 간 적이 없다면
                        runaway.append([nr, nc])
                        moved[nr][nc] = moved[r][c] + 1
                        cnt += 1

                elif k == 2:    # 왼쪽 탐색
                    if board[nr][nc] in left_lst[now] and moved[nr][nc] == 0:  # 갈 수 있는 길이고 간 적이 없다면
                        runaway.append([nr, nc])
                        moved[nr][nc] = moved[r][c] + 1
                        cnt += 1

                elif k == 3:    # 위쪽 탐색
                    if board[nr][nc] in up_lst[now] and moved[nr][nc] == 0:  # 갈 수 있는 길이고 간 적이 없다면
                        runaway.append([nr, nc])
                        moved[nr][nc] = moved[r][c] + 1
                        cnt += 1

    print(f'#{x}', cnt)
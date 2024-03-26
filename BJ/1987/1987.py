def dfs(arr):
    to_go = []
    visited = []
    max_len = 0

    to_go.append((0, 0, 1))    # 시작점 append. [r, c, cnt] 로 이루어짐

    while to_go:
        r, c, cnt = to_go.pop()

        if cnt <= len(visited):   # 분기점으로 돌아가기
            for _ in range(len(visited) + 1 - cnt):
                visited.pop()

        visited.append(arr[r][c])

        if cnt >= max_len:
            max_len = cnt # 길의 길이 업데이트

        for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr = r + direction[0]
            nc = c + direction[1]

            if 0 <= nr < R and 0 <= nc < C: # 행렬 내에 있고
                if arr[nr][nc] not in visited:  # 방문한 적이 없다면
                    to_go.append((nr, nc, cnt + 1))

    print(max_len)

import sys

R, C = map(int, input().split())
arr = [list(sys.stdin.readline()) for _ in range(R)]
dfs(arr)
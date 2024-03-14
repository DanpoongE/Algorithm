from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []
to_go = deque()
for r in range(N):
    for c in range(N):
        if visited[r][c] ==0 and arr[r][c] == 1:    # 간 적 없는 세대라면
            to_go.append([r, c])
            visited[r][c] = 1

            cnt = 0
            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]
            while to_go:
                i, j = to_go.popleft()
                cnt += 1

                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:  # 행렬 범위 내이고
                        if arr[ni][nj] == 1 and visited[ni][nj] == 0:        # 이어진 길이라면
                            to_go.append([ni, nj])  # 갈 곳으로 추가
                            visited[ni][nj] = 1     # 방문한것으로 표시
                        else:
                            visited[ni][nj] = 1     # 0이어도 방문한 것으로 표시

            ans.append(cnt)

ans.sort()
print(len(ans), end='\n')
print(*ans, sep='\n')
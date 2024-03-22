from collections import deque

def ripening(startpoint): # 시작점은 [f, r, c] 리스트로 받을 것임
    ff, i, j = startpoint
    # 상하좌우
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if ripen[ff][ni][nj] == 0:   # 안익은 토마토고
                if visited[ff][ni][nj] == 0:  # 방문한 적 없다면
                    to_go.append([ff, ni, nj])  # 갈 곳으로 넣고
                    ripen[ff][ni][nj] = ripen[ff][i][j] + 1    # 일차+1만큼의 숫자로 익었다고 표시
                    visited[ff][ni][nj] = 1 # 방문표시
    # 아래 위층
    df = [-1, 1]
    for p in range(2):
        nf = ff + df[p]
        if 0 <= nf < H:
            if ripen[nf][i][j] == 0:    # 안익은 토마토고
                if visited[nf][i][j] == 0:  # 방문한 적 없다면
                    to_go.append([nf, i, j])
                    ripen[nf][i][j] = ripen[ff][i][j] + 1
                    visited[nf][i][j] = 1

def isallripen(arr):
    for f in range(H):
        for r in range(N):
            for c in range(M):
                if ripen[f][r][c] == 0: # 안 익은 게 있다면
                    return -1

M, N, H = list(map(int, input().split()))
ripen = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
to_go = deque()

# 층, 행, 열을 순회하면서 익은 토마토(1) 찾기. 해당 토마토의 위치좌표 넣어두기
for f in range(H):
    for r in range(N):
        for c in range(M):
            if ripen[f][r][c] == 1:
                to_go.append([f, r, c])
                visited[f][r][c] = 1          # bfs는 to_go에 append 할 때 방문표시해줘야

while to_go:
    ripening(to_go.popleft())

if isallripen(ripen) == -1:
    print(-1)
else:
    ans = 0
    for f in range(H):
        for r in range(N):
            if max(ripen[f][r]) >= ans:
                ans = max(ripen[f][r])
    print(ans - 1)
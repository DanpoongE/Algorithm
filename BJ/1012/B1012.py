from collections import deque

def bfs():
    global q, visited
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while q:
        i, j = q.popleft()

        for v in range(4):
            ni = i + di[v]
            nj = j + dj[v]

            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1:    # 배추가 있으면
                    q.append((ni, nj))
                    visited.add((ni, nj))

T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    q = deque()
    visited = set()

    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1

    for rr in range(N):
        for cc in range(M):
            pass


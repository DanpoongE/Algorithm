from copy import deepcopy
from collections import deque

def melting(r, c):
    melt = 0

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M: # 행렬 내에 있고
            if arr[nr][nc] == 0: # 바다라면
                melt += 1
    
    if arr[r][c] - melt < 0:
        return 0
    else:
        return arr[r][c] - melt


def how_many_icebergs(arr):
    icebergs = 0
    visited = [[0] * M for _ in range(N)]
    to_go = deque()
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                if arr[i][j] != 0: # 빙하가 있는 곳이고 가본적 없으면 탐색 시작
                    to_go.append((i, j))
                    visited[i][j] = 1   # 방문 기록

                    while to_go:
                        si, sj = to_go.popleft()
                        for o in range(4):
                            ni = si + dr[o]
                            nj = sj + dc[o]
                            
                            if 0 <= ni < N and 0 <= nj < M:
                                if arr[ni][nj] != 0 and visited[ni][nj] == 0: # 육지이고 방문한 기록이 없으면 togo에 append, visited 기록
                                    to_go.append((ni, nj))
                                    visited[ni][nj] = 1
                    icebergs += 1
    return icebergs

            

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
years = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# if how_many_icebergs(arr) >= 2:
#     print(years)

# else:
while how_many_icebergs(arr) < 2:
    years += 1
    after_melt_arr = deepcopy(arr)

    for r in range(N):
        for c in range(M): # 행렬을 순회하면서
            if arr[r][c] != 0: # 바다가 아닌 경우
                after_melt_arr[r][c] = melting(r, c)    # melting 함수로 낮아진 높이 기록

    # after_melt_arr의 덩어리 개수 파악
    if how_many_icebergs(after_melt_arr) < 2:
        arr = after_melt_arr
        after_melt_arr = deepcopy(arr)
        
        if arr == [[0]*N for _ in range(M)]:
            years = 0
            break
    else:
        break
        
print(years)
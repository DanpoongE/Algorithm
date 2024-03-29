import sys
sys.stdin = open('B2468.txt')
from collections import deque

def find_safearea(i, j):  
    to_go = deque()
    to_go.append((i, j))
    visited[i][j] = 1

    while to_go:
        si, sj = to_go.popleft()    # 기준점 뽑고
        for k in range(4):          # 상하좌우 탐색
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < N and 0 <= nj < N: # 행렬 범위 내에 있고
                if visited[ni][nj] == 0:    # 온 적 없는 곳이고
                    if after_rain[ni][nj] == 1: # 안전 지역이라면
                        to_go.append((ni, nj))
                        visited[ni][nj] = 1


N = int(input())
hills = [list(map(int, input().split())) for _ in range(N)]
ans = 1

# 최댓값 찾기 -> 장마철 비의 양 최대치
max_height = 0
for i in range(N):      # 최대 100번 돎
    max_height = max(max(hills[i]), max_height)

for rain in range(1, max_height):
    after_rain = [[0] * N for _ in range(N)]    # 비가 내린 후 잠기는 지역 0, 안전지역 1으로 표시할 예정
    visited = [[0] * N for _ in range(N)]
    safe_area = 0

    # 비가 옵니다.
    for r in range(N):
        for c in range(N):
            if hills[r][c] > rain:    # 장마철 비 내리는 양보다 높이가 더 높다면
                after_rain[r][c] = 1
            # 봉우리의 높이가 더 낮다면 물에 잠김. 그대로 두면 됨

    # 자 이제 단지 찾듯이 이어진 부분 찾겠읍니다.
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for r in range(N):
        for c in range(N):
            if after_rain[r][c] == 0:   # 안전지역이 아니라면
                visited[r][c] = 1   # 방문표시만 하고 지나가기
            else:   # 안전지역이고
                if visited[r][c] == 0:   # 방문한 적 없다면
                    find_safearea(r, c)
                    safe_area += 1
    
    if safe_area > ans:
        ans = safe_area

print(ans)
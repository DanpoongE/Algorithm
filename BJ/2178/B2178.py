import sys
sys.stdin = open('B2178input.txt')
from collections import deque
 
N, M = list(map(int, input().split()))
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans_board = [[0] * M for _ in range(N)]
to_go = deque()

i = 0
j = 0
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
to_go.append([i, j])
ans_board[0][0] = 1

while visited[N - 1][M - 1] != 1:   # N, M에 도착할 때까지 
    if i == N - 1 and j == M - 1:
        break
    i, j = to_go.popleft()         # bfs
            
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<= ni < N and 0<= nj < M: # 행렬 내에 있고
            if arr[ni][nj] == 1 and visited[ni][nj] == 0:  # 갈 수 있는 길이며, 간 적이 없는 곳이라면
                visited[ni][nj] = 1       # BFS는 큐에 넣기 전에 방문표시를 해야 한다.
                to_go.append([ni, nj])
                if ans_board[ni][nj] <= ans_board[i][j] + 1:
                    ans_board[ni][nj] = ans_board[i][j] + 1 
        
print(ans_board[N - 1][M - 1])

# ans = []

# # 우측 우선탐색
# to_go = []
# visited = [[0] * M for __ in range(N)]
# pre_i = -1
# pre_j = 0
# i = 0
# j = 0
# cnt = 0
# di = [-1, 0, 1, 0]
# dj = [0, -1, 0, 1]
# to_go.append([i, j])
# while visited[N - 1][M - 1] != 1:   # N, M에 도착할 때까지 
#     i, j = to_go.pop()
#     visited[i][j] = 1       # 방문표시
#     cnt += 1
#     now_loc = [i, j]
#     if now_loc not in [[pre_i, pre_j + 1], [pre_i + 1, pre_j], [pre_i, pre_j - 1], [pre_i - 1, pre_j]]:
#             cnt -= 1
#     if i == N - 1 and j == M - 1:
#         ans.append(cnt)
#         break
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0<= ni < N and 0<= nj < M: # 행렬 내에 있고
#             if arr[ni][nj] == 1 and visited[ni][nj] == 0:  # 갈 수 있는 길이며, 간 적이 없는 곳이라면
#                 to_go.append([ni, nj])
#     pre_i = i
#     pre_j = j

# # 아래 우선탐색
# to_go = []
# visited = [[0] * M for __ in range(N)]
# pre_i = -1
# pre_j = 0
# i = 0
# j = 0
# cnt = 0
# di = [0, -1, 0, 1]
# dj = [1, 0, -1, 0]
# to_go.append([i, j])
# while visited[N - 1][M - 1] != 1:   # N, M에 도착할 때까지 
#     i, j = to_go.pop()
#     visited[i][j] = 1       # 방문표시
#     cnt += 1
#     now_loc = [i, j]
#     if now_loc not in [[pre_i, pre_j + 1], [pre_i + 1, pre_j], [pre_i, pre_j - 1], [pre_i - 1, pre_j]]:
#             cnt -= 1
#     if i == N - 1 and j == M - 1:
#         ans.append(cnt)
#         break
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0<= ni < N and 0<= nj < M: # 행렬 내에 있고
#             if arr[ni][nj] == 1 and visited[ni][nj] == 0:  # 갈 수 있는 길이며, 간 적이 없는 곳이라면
#                 to_go.append([ni, nj])
#     pre_i = i
#     pre_j = j

# print(min(ans))
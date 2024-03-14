def find_road(r, c, deduction):         # 시작점이 주어지면
    arr[r][c] -= deduction    # 1부터 K까지 깎아
    to_go = [[i, j]]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 0
    ans = []

    while to_go:
        si, sj = to_go.pop()
        cnt += 1
        for m in range(4):
            ni = si + di[m]
            nj = sj + dj[m]

            if 0 <= ni < N and 0 <= nj < N: # 행렬 범위 내의 값이고
                if arr[si][sj] > arr[ni][nj]:  # 새로 갈 곳이 더 낮고
                    if visited[ni][nj] == 0:    # 방문한 적이 없으면
                        to_go.append([ni, nj])

                else:  # 새로 갈 곳이 더 높으면
                    ans.append(cnt)

    return max(ans)


T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    M_hill = 0
    for r in arr:
        max_val = max(r)
        if max_val >= M_hill:
            M_hill = max_val

    startpoints = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == M_hill:
                startpoints.append([r, c])


    while startpoints:
        i, j = startpoints.pop()
        for r in range(N):
            for c in range(N):
                if r != i or c != j:    # 최정상 봉우리가 아닐 때
                    for kk in range(K + 1):
                        find_road(r, c, kk)

# def road(arr, i, j):
#     global flag
#     global cnt
#     to_go = [[i, j]]
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     ans = []
#
#     while to_go:
#         si, sj = to_go.pop()
#         visited[si][sj] = 1
#         for k in range(4):
#             ni = si + di[k]
#             nj = sj + dj[k]
#
#             if 0 <= ni < N and 0 <= nj < N:
#                 if arr[si][sj] > arr[ni][nj]:   # 새로 갈 곳이 더 낮고
#                     if visited[ni][nj] == 0:    # 방문한 적이 없으면
#                         to_go.append([ni, nj])
#                         length[ni][nj] = length[si][sj] + 1
#                         # cnt += 1
#
#                 else:                           # 새로 갈 곳이 더 높으면
#                     if flag == 1:               # 땅을 한번 깎을 수 있고
#                         if arr[ni][nj] - K < arr[si][sj]: # 깎았을 때 출발점보다 낮아질 수 있다면
#                             if visited[ni][nj] == 0:      # 방문한 적 없다면
#                                 arr[ni][nj] = arr[si][sj] - 1
#                                 flag = 0
#                                 to_go.append([ni, nj])
#                                 length[ni][nj] = length[si][sj] + 1
#                                 # cnt += 1
#
#                     else:   # 땅을 깎을 수 없다면
#                         ans.append(length[si][sj])
#     print(max(ans))

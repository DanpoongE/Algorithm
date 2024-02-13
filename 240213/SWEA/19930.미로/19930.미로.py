T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)] # 방문 여부를 저장하는 다른 행렬
    result = 0
    stack = []                          # 앞으로 방문할 좌표

    # 행렬을 순회하면서 시작점 좌표를 찾아줍니다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                 stack.append([i, j]) # 시작점 좌표 stack에 넣고
                 break

    # 시작점으로부터 상하좌우 탐색.
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    while stack:
        i, j = stack.pop()
        visited[i][j] = 1  # 방문점에 표시해주기

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:       # 행렬 내부의 점이고
                if arr[ni][nj] == 0:            # 주변 탐색하다가 0이고 방문한적 없으면
                    stack.append([ni, nj])      # 해당 위치 stack에 push
                    visited[ni][nj] = 1  # 방문표시 해주고 다시 돌자!
                    # ni, nj = stack.pop() # 새로운 탐색점

                elif arr[ni][nj] == 3:
                    result += 1
                    break
    for i in arr:
        print(i)

    print()
    for i in visited:
        print(i)

    print(f'#{tc} {result}')

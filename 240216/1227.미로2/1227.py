from collections import deque

T = 10

for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input())) for __ in range(100)]
    visited = [[0]*100 for ___ in range(100)]     # 방문한 곳 기록할 arr
    q = deque()
    # 앞으로 갈 곳

    # 첫 시작점 찾아 stack에 넣기
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                q.append([i, j])
                visited[i][j] = 1       # 그리고 enqueue할 때 방문표시하기
                break
        if q:                       # 시작점을 찾아 stack에 넣었다면
            break

    # stack이 빌 때까지 pop해서 탐색
    answer = 0

    while q:
        i, j = q.popleft()
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        for k in range(4):  # 우, 하, 좌, 상단 검색
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < 100 and 0 <= nj < 100:  # 행렬 범위 내에서
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:  # 길이 뚫려있고, 방문한 적이 없던 곳이라면
                    q.append([ni, nj])  # q에 넣고
                    visited[ni][nj] = 1  # 방문표시

                elif arr[ni][nj] == 3:
                    answer = 1

    print(f'#{tc} {answer}')
from collections import deque

def where_is_start(N, arr):
    startpoint = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                startpoint.extend([i, j])
                return startpoint

        if startpoint:
            break


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for __ in range(N)]

    # 시작점을 찾고, 0인 곳을 to_go에 push
    to_go = deque()
    to_go.append(where_is_start(N, arr))
    # 시작점에 거리 함께 넣어주기
    to_go[0].append(0)

    # 탐색 준비
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    done = False
    answer = 0

    while to_go:
        i, j, dist = to_go.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                # 행렬 내 뚫린 길이라면
                if arr[ni][nj] == 0:
                    to_go.append([ni, nj, dist+1]) #push 하고
                    arr[ni][nj] = 1 # 방문했다는 표시로 1로 바꾸기

                elif arr[ni][nj] == 3:
                    to_go.clear()
                    answer = dist
                    done = True
                    break

        if done:
            break

    if not done:        # 도착지점과 연결되어 있다면
        answer = 0


    print(f'#{tc} {answer}')



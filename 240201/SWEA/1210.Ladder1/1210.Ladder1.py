T = 10
N = 100
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, -1]
    dj = [-1, 1, 0]

    i = 99
    j = arr[99].index(2)    # 현재 위치 index 찾음!

    while i != 0:           # 행 index 0이 되기 전까지
        if 0<=i+di[0]<N and 0<=j+dj<N and arr[i+di[0]][j+dj[0]] == 1:       # 왼쪽 먼저 봅시다.
            arr[i][j] = 0
            i = i+di[0]
            j = j+dj[0]


        elif 0<=i+di[0]<N and 0<=j+dj<N and arr[i+di[1]][j+dj[1]] == 1: # 오른쪽 볼게용
            arr[i][j] = 0
            i = i+di[1]
            j = j+dj[1]

        else:                                                           # 둘 다 0이면 위 갈게용
            arr[i][j] = 0
            i = i+di[2]
            j = j+dj[2]

    print(f'#{tc} {i}')















    # for j in range(N):              # 마지막행 중에서
    #     if arr[99][j] == 2:         #  2 값을 가지는 도착점
    #         row = 99
    #         col = j                 # 찾았으면 해당 변수에 기록하고
    #         break                   # 브레이끼
    #
    # direction = "top"
    # while row != 0:
    #     # 위로 이동한 경우에는 좌우를 먼저 확인
    #     if direction == 'left':  # 왼쪽으로 이동하는거면 열 인덱스 -1
    #         col -= 1
    #         if arr[row - 1][col] == 1: #왼쪽으로 옮겨간 후 위를 확인했을 때 1이면
    #             direction = 'top' # 위로 갑니다.
    #             continue
    #
    #     elif direction == 'right': #그러나 오른쪽으로 이동하는거면
    #         col += 1        # 행 인덱스 +1
    #         if arr[row - 1][col] == 1: #오른쪽으로 옮겨간 후 위를 확인했을 때 1이면
    #             direction = 'top' # 마찬가지. top으로 갑니다.
    #             continue
    #     else:           # 좌우 이동을 한 경우라면 위를 먼저 확인.
    #         row -= 1    # 좌우 이동이 아니라면 한칸 위로.
    #         if col - 1 >= 0: #좌측 위로 이동한 후, 열의 index가 0이상이면
    #             if arr[row][col-1] == 1: # 좌측을 확인합니다.
    #                 direction = 'left'
    #                 continue
    #         if col + 1 < 100: #우측 위로 이동한 후, 열의 index가 100 미만이면
    #             if arr[row][col+1] == 1: # 우측을 확인합니다.
    #                 direction = 'right'
    #                 continue
    # print(f'#{tc} {col}')

















    #
    # i = 99                          # 출발점은 마지막행만 확인.
    # for j in range(N):
    #     if arr[i][j] == 2:              # 도착점이 2이면
    #         col = j
    #         break
    # if arr[i-1][current_j] == 0: # 위가 0으로 막혔을 때
    # for dj in [-1, 1]:          # 양 옆을 확인할거야(열)
    #     nj = current_j + dj     # 새로운 열 인덱스 nj
    #     if 0 <= nj < N:         # nj 범위가 행렬에서 벗어나지 않게
    #         if arr[i][nj] == 1: # 확인했더니 양 옆이 1이라면
    #             temp_j = nj
    #     else:
    #         i -= 1
    #                                     # 양 옆을 먼저 확인
    # print(i, temp_j)

            # 그 다음에 양 옆을 계속 확인하면서 1이 뜨면 꺾어.
    # print(f'#{tc} {arr}')


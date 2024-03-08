T = int(input())
for x in range(1):
    N, M, K = list(map(int, input().split()))
    colonies = [list(map(int, input().split())) for _ in range(K)]

    for isolate in range(1): # 격리시간동안
        for lst in colonies:        # 군집 lst들 순회하면서
            if lst[3] == 1:     # 방향이 위쪽이고
                if lst[0] - 1 == 0: # 이동시 경계면
                    lst[0] -= 1
                    lst[2] //= 2
                    lst[3] = 2  # 방향 아래로 전환
                else:
                    lst[0] -= 1
            elif lst[3] == 2:   # 방향이 아래쪽이고
                if lst[0] + 1 == N - 1: # 이동시 경계면
                    lst[0] += 1
                    lst[2] //= 2
                    lst[3] = 1  # 방향 위로 전환
                else:
                    lst[0] += 1
            elif lst[3] == 3:   # 방향이 왼쪽이고
                if lst[1] - 1 == 0: # 이동시 경계면
                    lst[1] -= 1
                    lst[2] //= 2
                    lst[3] = 4 # 방향 오른쪽으로 전환
                else:
                    lst[1] -= 1
            else:   # 방향이 오른쪽이고
                if lst[1] + 1 == N - 1:
                    lst[1] += 1
                    lst[2] //= 2
                    lst[3] = 3  # 방향 왼쪽으로 전환
                else:
                    lst[1] += 1
        colonies.sort()

# def boar_changes(N, M, board, direction_board):
#     merge = []
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] > 0: # 미생물 군집이 있고
#                 if direction_board[i][j] == 1:  # 위쪽으로 이동한다면
#                     if i - 1 == 0:  # 약품이 칠해진 외곽이라면
#                         board[i - 1][j] = board[i][j] // 2
#                         board[i][j] = 0     # 원래 자리는 clear
#                         direction_board[i - 1][j] = 2   # 방향 반대로 바뀜
#                         direction_board[i][j] = 0   # 원래 자리의 방향도 clear
#                     else:   # 그냥 내부라면
#                         board[i - 1][j] += board[i][j]
#                         direction_board[i - 1][j] = 1   # 위로 이동
#                         from_up = board[i][j]
#                         if board[i - 1][j] > board[i][j]:   # 원래 있었던 값보다 크다면 여러 군집이 합쳐진 거
#                             merge.append(from_up)
#                         board[i][j] = 0 # 원래 자리 clear
#                         direction_board[i][j] = 0   # 원래 자리의 방향도 clear
#
#                 elif direction_board[i][j] == 2: # 아래쪽으로 이동한다면
#                     if i + 1 == N - 1:  # 약품이 칠해진 외곽이라면
#                         board[i + 1][j] = board[i][j] // 2
#                         board[i][j] = 0     # 원래 자리는 clear
#                         direction_board[i + 1][j] = 1   # 방향 반대로 바뀜
#                         direction_board[i][j] = 0   # 원래 자리의 방향도 clear
#                     else:   # 그냥 내부라면
#                         board[i + 1][j] += board[i][j]
#                         direction_board[i + 1][j] = 2   # 아래로 이동
#                         from_down = board[i][j]
#                         if board[i + 1][j] > board[i][j]:   # 원래 있었던 값보다 크다면 여러 군집이 합쳐진 거
#                             merge.append(from_down)
#                         board[i][j] = 0 # 원래 자리 clear
#                         direction_board[i][j] = 0   # 원래 자리의 방향도 clear
#
#                 elif direction_board[i][j] == 3:  # 왼쪽으로 이동한다면
#
#                 else:   # 오른쪽으로 이동한다면

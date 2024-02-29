import sys
input = sys.stdin.readline
C, R = list(map(int, input().split()))
K = int(input())

if C * R < K:
    print(0)

else:
    seat_arr = [[0] * C for _ in range(R)]
    people = 1
    way_to_go = 'up'
    # 시작점
    i = R - 1
    j = 0
    full_flag = 0

    while people <= K:
        seat_arr[i][j] = people
        if people == R * C:
            people += 1
            full_flag += 1
            break
        # 이전에 아래에서 위로 올라왔고 & 위가 행렬 범위고 & 차 있지 않다면 (위로 간다):
        if way_to_go == 'up':
            if i - 1 >= 0 and seat_arr[i - 1][j] == 0:
                i -= 1
                people += 1
            else:   # 아니라면 오른쪽으로 갈 차례.
                way_to_go = 'right'

        # 오른쪽으로 갈 차례고 & 행렬 범위 내 & 차 있지 않다면 (오른쪽으로 간다)
        elif way_to_go == 'right':
            if j + 1 < C and seat_arr[i][j + 1] == 0:
                j += 1
                people += 1
            else:   # 아니라면 아래로 갈 차례.
                way_to_go = 'down'

        elif way_to_go == 'down':
            if i + 1 < R and seat_arr[i + 1][j] == 0:
                i += 1
                people += 1
            else:
                way_to_go = 'left'

        elif way_to_go == 'left':
            if j - 1 >= 0 and seat_arr[i][j - 1] == 0:
                j -= 1
                people += 1
            else:
                way_to_go = 'up'

    # 이미 다음 좌석 넘버와 대기 순서로 넘어간 상태.
    if full_flag == 0:
        if way_to_go == 'up':
            i += 1
        elif way_to_go == 'right':
            j -= 1
        elif way_to_go == 'down':
            i -= 1
        else:
            j += 1

    x = j + 1
    y = R - i
    print(x, y)
T = int(input())

for x in range(1, T + 1):
    N = int(input())        # 방의 한 변의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    people_idx = []
    people_num = 0
    exit_idx = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people_idx.append([i, j])
                people_num += 1
            elif arr[i][j] > 1:
                exit_idx.append([i, j])

    #계단 도착시간
    arrival1 = []
    arrival2 = []
    for ii in range(people_num):
        dis1 = abs(people_idx[ii][0] - exit_idx[0][0]) + abs(people_idx[ii][1] - exit_idx[0][1])
        arrival1.append(dis1)
        dis2 = abs(people_idx[ii][0] - exit_idx[1][0]) + abs(people_idx[ii][1] - exit_idx[1][1])
        arrival2.append(dis2)
    print(arrival1)
    print(arrival2)
    print('------------------------')
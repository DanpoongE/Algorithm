T = 10

for tc in range(1, T+1):
    M = int(input())
    arr = [list(input()) for _ in range(8)]

    # print(arr)

    # 행 확인
    row_count = 0
    for i in range(8):
        for j in range(8-M+1):
            new_list = []
            for z in range(M):
                new_list.append(arr[i][j+z])

            print(new_list)

            # rev_list = list(reversed(new_list))
            #
            #
            # if new_list == rev_list:
            #     row_count += 1
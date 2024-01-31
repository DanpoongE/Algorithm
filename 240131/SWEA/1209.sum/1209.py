TC = 10
N = 100

for tc in range(TC):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sums = []

    # 각 행의 총합 (100개)
    line1 = line2 = 0
    for i in range(N):
        sums.append(sum(arr[i]))

    # 각 열의 총합 (100개)
        col = 0
        for j in range(N):
            col += arr[j][i]
            sums.append(col)

    # 두 대각선의 총합 (2개)
        line1 += arr[i][i]
        line2 += arr[i][N-1-i]
        sums.append(line1)
        sums.append(line2)

    # sums에서 최댓값 찾아주기
    print(f'#{t} {max(sums)}')

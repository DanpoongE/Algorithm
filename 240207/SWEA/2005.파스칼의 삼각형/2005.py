T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []

    for x in range(1, N+1):
        arr.append([0]*x)
    # arr = [[0] for _ in range(N)] 이렇게 해서 만드는 방법은 없나?

    for i in range(N):
        for j in range(N):
            if i >= j:
                if j == 0 or j == i:
                    arr[i][j] = 1
                # 이거 메모이제이션해볼까?
                else:
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    # break

    print(f'#{tc}')
    # for z in range(N):
    #     print(*arr[z])

    for z in arr:
        print(*z)
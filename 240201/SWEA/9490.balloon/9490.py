T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(M):
            counts = arr[i][j]
            move = arr[i][j]
            for di in range(1, move + 1): # 같은 행 팡팡!
                if 0 <= i+di < N:
                    counts += arr[i+di][j]
                if 0 <= i-di < N:
                    counts += arr[i-di][j]
            for dj in range(1, move + 1):
                if 0 <= j+dj < M:
                    counts += arr[i][j+dj]
                if 0 <= j-dj < M:
                    counts += arr[i][j-dj]

            result.append(counts)

    print(f'#{tc} {max(result)}')
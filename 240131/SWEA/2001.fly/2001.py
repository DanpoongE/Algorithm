T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_fly = []

    for i in range(N):
        for j in range(N):
            fly = 0
            for di in range(M):
                ni = i + di
                for dj in range(M):
                    nj = j + dj
                    if 0<= ni <N and 0<= nj <N:
                        fly += arr[ni][nj]
                        sum_fly.append(fly)

    print(f'#{t} {max(sum_fly)}')
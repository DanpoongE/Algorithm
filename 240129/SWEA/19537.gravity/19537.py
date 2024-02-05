T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = []
    for i in range(N):
        move = 0
        for di in range(1, N):
            if 0<= i+di < N and arr[i] > arr[i+di]:
                move += 1
        cnt.append(move)

    print(f'#{tc} {max(cnt)}')

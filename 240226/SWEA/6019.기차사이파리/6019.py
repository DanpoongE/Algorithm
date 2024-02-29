T = int(input())

for tc in range(1, T + 1):
    D, A, B, F = list(map(int, input().split()))

    collide = D / (A + B)

    result = collide * F

    print(f'#{tc}', result)
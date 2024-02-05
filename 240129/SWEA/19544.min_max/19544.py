T = int(input())

for tc in range (1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_val = max(arr)
    min_val = min(arr)

    result = max_val - min_val

    print(f'#{tc} {result}')
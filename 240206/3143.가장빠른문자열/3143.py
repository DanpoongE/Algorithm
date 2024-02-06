T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    result = A.replace(B, 'x')
    print(f'#{tc} {len(result)}')

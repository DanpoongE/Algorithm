from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = deque(map(int, input().split()))

    # print(numbers)
    i = M % N

    for _ in range(i):    # i번 돌린당
        numbers.append(numbers.popleft())

    print(f'#{tc}', numbers[0])

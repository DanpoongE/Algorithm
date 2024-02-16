from collections import deque

def cycle(a):
    for i in range(1, 6):      # 1부터 뺄건데
        a[0] -= i        # 첫번째 숫자 i만큼 감소시키기
        if a[0] <= 0:       # 그 결과 음수이거나 0이면
            a[0] = 0        # 0으로 해주고
            a.append(a.popleft())
            break
        a.append(a.popleft()) # 맨 앞쪽 수 빼서 뒤로 가자~

    return a


T = 10

for _ in range(1, T+1):
    tc = int(input())
    numbers = deque(map(int, input().split()))
    # print(numbers.popleft())

    while numbers[-1] != 0:     # 맨 뒤 숫자가 0이면 stop
        cycle(numbers)

    print(f'#{tc}', *numbers)


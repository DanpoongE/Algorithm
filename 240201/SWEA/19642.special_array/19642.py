T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(5):
        print(arr[-(i+1)], arr[i], end='')

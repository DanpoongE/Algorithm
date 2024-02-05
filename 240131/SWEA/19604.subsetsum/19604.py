A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())

for _ in range(T):
    N, K = list(map(int, input().split()))

    cnts = [0]*N

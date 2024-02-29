import sys
input = sys.stdin.readline
N, K = list(map(int, input().split()))
weather = list(map(int, input().split()))
start_sum = sum(weather[0:0+K])
max_sum = start_sum

for i in range(N - K):
    next_sum = start_sum - weather[i] + weather[i + K]
    if max_sum <= next_sum:
        max_sum = next_sum
    start_sum = next_sum

print(max_sum)


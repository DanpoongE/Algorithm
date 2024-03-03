import sys
sys.stdin = open('B2491input.txt')

N = int(input())        # 수열의 길이
arr = list(map(int, input().split()))

up_going = 1
down_going = 1
ans = []
for i in range(N - 1):
    if arr[i] <= arr[i + 1]:
        up_going += 1
    else:
        ans.append(up_going)
        up_going = 1
ans.append(up_going)

for i in range(N - 1):
    if arr[i] >= arr[i + 1]:
        down_going += 1
    else:
        ans.append(down_going)
        down_going = 1
ans.append(down_going)

if up_going == len(arr):
    ans.append(up_going)

if down_going == len(arr):
    ans.append(down_going)

print(max(ans))
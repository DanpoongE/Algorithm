N = 3
arr = [1, 2, 3]

for i in range(1<<N):   #2의 N제곱이라는 의미, 공집합을 제거하려면 (1, 1<<N)
    s = 0
    for j in range(N): #j번 비트를 이용해 j
        if i&(1<<j):
            s += arr[j]
            print(arr[j], end= ' ')
    print(s)
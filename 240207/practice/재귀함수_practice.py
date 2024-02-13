def f(i, k): # i 현재위치, k 목표
    if i==k:
        return
    else:
        print(arr[i])
        f(i+1, k)


arr = [10, 20, 30]
N = len(arr)
f(0, N)
# 10
# 20
# 30

# 이거 for문으로 할 줄은 아는데 재귀함수 쓰는건 익숙지 않아서 기억해두기